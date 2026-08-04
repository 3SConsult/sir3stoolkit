"""Minimal MCP-style server entrypoint template.

This file exposes a generic request router and supports startup initialization
of sir3stoolkit from either a CLI argument or an environment variable.
"""

from __future__ import annotations

import argparse
import os
from typing import Any

from .tools import TOOLS, initialize_toolkit

SIRGRAF_ENV_VAR = "SIR3S_SIRGRAF_DIR"


def handle_request(request: dict[str, Any]) -> dict[str, Any]:
    """Route one structured request to a registered tool."""
    tool_name = request.get("tool")
    args = request.get("args", {})

    if not tool_name:
        return {
            "status": "error",
            "error_code": "MISSING_TOOL",
            "message": "Request must include 'tool'.",
        }

    if tool_name not in TOOLS:
        return {
            "status": "error",
            "error_code": "UNKNOWN_TOOL",
            "message": f"Unknown tool: {tool_name}",
        }

    try:
        result = TOOLS[tool_name](**args)
        return {
            "status": "ok",
            "result": result,
        }
    except Exception as ex:
        return {
            "status": "error",
            "error_code": "TOOL_EXECUTION_FAILED",
            "message": str(ex),
        }


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="sir3stoolkit-mcp",
        description="sir3stoolkit MCP server template",
    )
    parser.add_argument(
        "--sirgraf-dir",
        dest="sirgraf_dir",
        default=None,
        help=(
            "Path to the local SirGraf installation directory. "
            f"If omitted, environment variable {SIRGRAF_ENV_VAR} is used."
        ),
    )
    return parser.parse_args(argv)


def _resolve_sirgraf_dir(cli_value: str | None) -> str | None:
    if cli_value:
        return cli_value
    return os.getenv(SIRGRAF_ENV_VAR)


def _bootstrap_toolkit(sirgraf_dir: str | None) -> tuple[bool, str]:
    if not sirgraf_dir:
        return (
            False,
            "SirGraf directory is required. Provide --sirgraf-dir or set "
            f"{SIRGRAF_ENV_VAR}.",
        )

    init_result = initialize_toolkit(sirgraf_dir)
    if init_result.get("status") != "ok":
        return False, str(init_result)

    return True, f"Toolkit initialized with SirGraf directory: {sirgraf_dir}"


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint placeholder.

    Replace this with your MCP framework bootstrap (stdio/http) when ready.
    """
    args = _parse_args(argv)
    sirgraf_dir = _resolve_sirgraf_dir(args.sirgraf_dir)
    ok, message = _bootstrap_toolkit(sirgraf_dir)
    if not ok:
        print(f"Startup failed: {message}")
        return 1

    print(message)
    print("sir3stoolkit MCP template is installed.")
    print("Implement transport startup in sir3stoolkit.mcp.server:main")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
