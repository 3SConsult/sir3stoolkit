# -*- coding: utf-8 -*-
"""Command line of sir3stoolkit: ``python -m sir3stoolkit <command>``, see ``python -m sir3stoolkit -h``."""

import argparse
import sys

from sir3stoolkit import ai_guide


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="python -m sir3stoolkit", description="sir3stoolkit command line.")
    commands = parser.add_subparsers(dest="command", required=True, metavar="command")

    setup = commands.add_parser(
        "ai-setup",
        help="add a pointer to the guide for AI assistants to a project's AGENTS.md (and CLAUDE.md)",
        description="Adds a short pointer to the guide for AI assistants (AGENTS.md shipped with the installed "
                    "sir3stoolkit) to the project's AGENTS.md (created if missing) and to its CLAUDE.md, if it has "
                    "one - AI coding agents load these files automatically. Re-run to update; only the marked "
                    "sir3stoolkit block is changed.")
    setup.add_argument("project_dir", nargs="?", default=".", help="project folder (default: current folder)")
    setup.add_argument("--remove", action="store_true", help="remove the pointer again")

    args = parser.parse_args(argv)
    if args.command == "ai-setup":
        try:
            results = ai_guide.ai_setup(args.project_dir, remove=args.remove)
        except (ValueError, NotADirectoryError) as e:
            print(e, file=sys.stderr)
            return 1
        for path, status in results.items():
            print(f"{status:>13}: {path}")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
