"""Subcommand dispatcher for the aff CLI."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from affidavit.verdict import run_verdict


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aff",
        description="aff CLI. The only command is verdict.",
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
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.command == "verdict":
        work = Path(args.cwd) if args.cwd else Path.cwd()
        payload = run_verdict(work, args.at, args.base, args.claim_ids)
        print(json.dumps(payload, separators=(",", ":")))
        return 0 if payload["result"] == "pass" else 1
    parser.error(f"unknown command {args.command!r}")
    return 2
