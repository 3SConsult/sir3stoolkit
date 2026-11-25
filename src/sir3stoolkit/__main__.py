# -*- coding: utf-8 -*-
"""Command line of sir3stoolkit: ``python -m sir3stoolkit <command>``, see ``python -m sir3stoolkit -h``."""

import argparse
import sys
import tempfile

from pathlib import Path

from sir3stoolkit import ai_guide, tutorials


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

    tut = commands.add_parser(
        "tutorials",
        help="download the tutorials (notebooks + models) of the installed version into a folder",
        description="Downloads the tutorials of sir3stoolkit - the notebooks and the SIR 3S models they use - "
                    "from the GitHub release of the installed version and unpacks them into a folder "
                    "(SIR3S_Model/TutorialNNN_Assets, SIR3S_Model_Mantle/TutorialNNN_Assets). Run the tutorials "
                    "from there: they change their models and write calculation results next to them.")
    tut.add_argument("folder", nargs="?", default=tutorials.DEFAULT_FOLDER,
                     help=f"folder to unpack into (default: ./{tutorials.DEFAULT_FOLDER})")
    tut.add_argument("--only", choices=sorted(tutorials.GROUPS),
                     help="only the core tutorials (0-49) or only the mantle tutorials (50-99)")
    tut.add_argument("--version", help="sir3stoolkit version whose tutorials to download (default: the installed one)")
    tut.add_argument("--overwrite", action="store_true",
                     help="replace files that already exist (default: keep them - the tutorials change their models)")
    tut.add_argument("--sirgraf-dir", metavar="PATH",
                     help="SirGraf folder to set in the notebooks (default: the one configured with "
                          "wrapper.Write_SirGraf_Config_Path(), if any)")

    args = parser.parse_args(argv)
    if args.command == "tutorials":
        groups = [args.only] if args.only else list(tutorials.GROUPS)
        if args.sirgraf_dir and not Path(args.sirgraf_dir).is_dir():
            print(f"SirGraf folder not found: {args.sirgraf_dir}", file=sys.stderr)
            return 1
        sirgraf_dir = args.sirgraf_dir or tutorials.get_configured_sirgraf_dir() or ""
        target = Path(args.folder).resolve()
        try:
            urls = [tutorials.get_tutorials_url(group, args.version) for group in groups]
            target.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryFile(dir=target):  # writable? - checked before downloading
                pass
            print(f"Downloading {', '.join(url.rsplit('/', 1)[1] for url in urls)} "
                  f"(release {urls[0].rsplit('/', 2)[1]}) into {target} ...", flush=True)
            result = tutorials.download_tutorials(target, groups=groups, version=args.version,
                                                  overwrite=args.overwrite, sirgraf_dir=sirgraf_dir)
        except (ValueError, ConnectionError) as e:
            print(e, file=sys.stderr)
            return 1
        except OSError as e:  # e.g. no permission, disk full
            where = e.filename or target
            print(f"Cannot write to {where}: {e.strerror or e} - choose another folder, "
                  f"e.g. python -m sir3stoolkit tutorials %USERPROFILE%\\sir3stoolkit_tutorials", file=sys.stderr)
            return 1
        print(f"Tutorials in {target}: {len(result['written'])} file(s) written", end="")
        print(f", {len(result['kept'])} existing file(s) kept (--overwrite replaces them)." if result["kept"] else ".")
        if result["sirgraf_dir_set"]:
            print(f"SIR3S_SIRGRAF_DIR set to {sirgraf_dir} in {len(result['sirgraf_dir_set'])} notebook(s).")
        if not sirgraf_dir:
            print("In each notebook, set SIR3S_SIRGRAF_DIR to your SirGraf folder - or store it once with "
                  "wrapper.Write_SirGraf_Config_Path() (Tutorial 0), then new downloads get it automatically.")
        return 0
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
