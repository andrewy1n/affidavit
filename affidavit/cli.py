"""Subcommand dispatcher for the aff CLI."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from affidavit.lint import find_new_skips, find_no_assert
from affidavit.verdict import run_verdict


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aff",
        description="aff CLI: verdict and witness lint.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    verdict = sub.add_parser(
        "verdict",
        help="Re-execute frozen oracle tests at two revisions",
    )
    verdict.add_argument(
        "--cwd",
        default=None,
        help="Git repository (default: process cwd)",
    )
    verdict.add_argument("--at", required=True, help="Revision where oracle tests must pass")
    verdict.add_argument(
        "--base",
        default=None,
        help="Revision where oracle tests must fail on an assertion (default: merge-base with main)",
    )
    verdict.add_argument("claim_ids", nargs="+", metavar="CLAIM", help="Claim ids to judge")

    lint = sub.add_parser("lint", help="Report no-assert witnesses or new skips")
    lint_sub = lint.add_subparsers(dest="lint_command", required=True)

    no_assert = lint_sub.add_parser(
        "no-assert",
        help="Report witness tests with no assert or pytest.raises",
    )
    no_assert.add_argument(
        "paths",
        nargs="+",
        metavar="PATH",
        help="Witness test source files to scan",
    )

    new_skips = lint_sub.add_parser(
        "new-skips",
        help="Report claim witnesses skipped at head but not at base",
    )
    new_skips.add_argument(
        "--cwd",
        default=None,
        help="Git repository (default: process cwd)",
    )
    new_skips.add_argument("--base", required=True, help="Base revision")
    new_skips.add_argument("--head", required=True, help="Head revision")
    new_skips.add_argument("claim_id", metavar="CLAIM", help="Claim id whose witnesses to compare")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.command == "verdict":
        work = Path(args.cwd) if args.cwd else Path.cwd()
        payload = run_verdict(work, args.at, args.base, args.claim_ids)
        print(json.dumps(payload, separators=(",", ":")))
        return 0 if payload["result"] == "pass" else 1
    if args.command == "lint":
        if args.lint_command == "no-assert":
            findings = find_no_assert([Path(p) for p in args.paths])
            for item in findings:
                print(item)
            return 1 if findings else 0
        if args.lint_command == "new-skips":
            work = Path(args.cwd) if args.cwd else Path.cwd()
            findings = find_new_skips(
                work, args.base, args.head, claim_id=args.claim_id
            )
            for item in findings:
                print(item)
            return 1 if findings else 0
        parser.error(f"unknown lint command {args.lint_command!r}")
    parser.error(f"unknown command {args.command!r}")
    return 2
