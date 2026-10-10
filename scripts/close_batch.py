#!/usr/bin/env python3
"""Build the NDJSON `apply` batch that closes a work-item.

Reads a close-request JSON describing the work-item's active acceptances,
each criterion's evidence, and the transition to apply.

For `method` `tdd` or `check`, the binary check-run must already exist
(from `se-workflow check`). The request references that runner-produced
`check_run_id` and copies its `result` for the refusal gate — this
script does not invent pass/fail or emit a `project:check-run` create
for those methods.

For `method` `manual`, the request carries `result` / `revision` /
`signed_by` and this script emits one `project:check-run` create per
entry (linked `informed_by` both its acceptance and the
execution-report when there is one).

An optional `project:finding` and the work-item transition follow, in
that order -- ready to feed straight into `adaptive-artifacts apply`.

What it enforces: closing to `done` while a criterion is unmet or was
never checked requires a `finding` in the same request, or the batch
is refused outright rather than silently written without one.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

RUNNER_METHODS = frozenset({"tdd", "check"})


class CloseRequestError(Exception):
    """Malformed close-request -- exit 1, distinct from a policy refusal."""


class CloseRefused(Exception):
    """Policy refusal -- exit 2, distinct from a malformed request."""


def _entry_passed(entry: dict[str, Any]) -> bool:
    return entry.get("result") == "pass"


def build_batch(request: dict[str, Any]) -> list[dict[str, Any]]:
    try:
        subject = request["subject"]
        effort = request["effort"]
        work_item_id = request["work_item_id"]
        transition = request["transition"]
        acceptance_ids = list(request["acceptance_ids"])
        criteria = list(request.get("criteria", []))
    except KeyError as exc:
        raise CloseRequestError(f"missing field: {exc}") from exc

    execution_report_id = request.get("execution_report_id")
    finding = request.get("finding")

    for entry in criteria:
        criterion_id = entry.get("criterion_id")
        if criterion_id not in acceptance_ids:
            raise CloseRequestError(
                f"criteria entry {criterion_id!r} is not in acceptance_ids {acceptance_ids}"
            )
        method = entry.get("method")
        if method is None:
            raise CloseRequestError("criteria entry missing field: 'method'")
        if method in RUNNER_METHODS:
            if not entry.get("check_run_id"):
                raise CloseRequestError(
                    f"criteria entry {criterion_id!r} method={method!r} must "
                    "reference a runner-produced check_run_id (from "
                    "se-workflow check); do not invent pass/fail"
                )
            if "result" not in entry:
                raise CloseRequestError(
                    f"criteria entry {criterion_id!r} method={method!r} must "
                    "copy result from the runner check-run"
                )
            # Invented create shape: revision/signed_by without going through
            # the runner — refuse so agents cannot smuggle a hand-authored
            # binary check-run through close.
            if "revision" in entry or "signed_by" in entry:
                raise CloseRequestError(
                    f"criteria entry {criterion_id!r} method={method!r} must "
                    "not carry revision/signed_by; reference check_run_id only"
                )
        elif method == "manual":
            for field in ("result", "revision"):
                if field not in entry:
                    raise CloseRequestError(
                        f"criteria entry missing field: '{field}'"
                    )
            if entry.get("check_run_id"):
                raise CloseRequestError(
                    f"criteria entry {criterion_id!r} method=manual must not "
                    "carry check_run_id; create the manual check-run via the batch"
                )
        else:
            raise CloseRequestError(
                f"criteria entry {criterion_id!r} has unknown method {method!r}"
            )

    passed_ids = {
        entry["criterion_id"] for entry in criteria if _entry_passed(entry)
    }
    unmet = [aid for aid in acceptance_ids if aid not in passed_ids]

    if transition == "done" and unmet and not finding:
        raise CloseRefused(
            "closing to done with unmet or unverified criterion(s) "
            f"{unmet} and no finding -- refusing. Either resolve those "
            "criteria first, or supply `finding` (claim, basis, "
            "invalidated_when, body) to close anyway."
        )

    ops: list[dict[str, Any]] = []
    for entry in criteria:
        method = entry["method"]
        if method in RUNNER_METHODS:
            # Runner already wrote the check-run; do not invent another.
            continue
        payload = {
            "criterion_id": entry["criterion_id"],
            "revision": entry["revision"],
            "result": entry["result"],
            "effort": effort,
            "method": method,
            "signed_by": entry.get("signed_by", ""),
        }
        rels = [f"informed_by:{entry['criterion_id']}"]
        if execution_report_id:
            rels.append(f"informed_by:{execution_report_id}")
        ops.append(
            {
                "op": "create",
                "type": "project:check-run",
                "subject": subject,
                "payload": payload,
                "rel": rels,
            }
        )

    if finding:
        try:
            finding_payload = {
                "claim": finding["claim"],
                "basis": finding["basis"],
                "invalidated_when": finding["invalidated_when"],
                "effort": effort,
                # Hardcoded, not passed through: this finding exists to
                # surface a deferred/unmet criterion under handoff's Needs
                # Human role, which only fires on needs="human".
                "needs": "human",
            }
            finding_body = finding["body"]
        except KeyError as exc:
            raise CloseRequestError(f"finding missing field: {exc}") from exc
        ops.append(
            {
                "op": "create",
                "type": "project:finding",
                "subject": subject,
                "payload": finding_payload,
                "body": finding_body,
            }
        )

    ops.append(
        {
            "op": "update",
            "type": "project:work-item",
            "id": work_item_id,
            "transition": transition,
            "expected_revision": "@current",
        }
    )
    return ops


def _read(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _write(path: str, text: str) -> None:
    if path == "-":
        sys.stdout.write(text)
        return
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", default="-", help="close-request JSON path, or '-' for stdin (default)"
    )
    parser.add_argument(
        "--out", default="-", help="NDJSON output path, or '-' for stdout (default)"
    )
    args = parser.parse_args(argv)

    try:
        request = json.loads(_read(args.input))
    except json.JSONDecodeError as exc:
        print(f"close-request is not valid JSON: {exc}", file=sys.stderr)
        return 1

    try:
        ops = build_batch(request)
    except CloseRefused as exc:
        print(f"close refused: {exc}", file=sys.stderr)
        return 2
    except CloseRequestError as exc:
        print(f"close-request malformed: {exc}", file=sys.stderr)
        return 1

    _write(args.out, "\n".join(json.dumps(op) for op in ops) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
