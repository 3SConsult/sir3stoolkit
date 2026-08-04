from __future__ import annotations

import argparse
import ast
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _path_to_module(src_root: Path, file_path: Path) -> str:
    rel = file_path.relative_to(src_root)
    parts = list(rel.with_suffix("").parts)
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _collect_defined_rows_from_file(file_path: Path, src_root: Path) -> list[dict[str, Any]]:
    source = file_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(file_path))
    module = _path_to_module(src_root, file_path)

    rows: list[dict[str, Any]] = []

    def visit_class(node: ast.ClassDef, stack: list[str]) -> None:
        qualname = ".".join([*stack, node.name]) if stack else node.name
        class_id = f"{module}.{qualname}"

        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                rows.append(
                    {
                        "method_name": item.name,
                        "defined_in_class_id": class_id,
                        "defined_in_class": qualname,
                        "defined_in_module": module,
                        "defined_in_file": str(file_path),
                        "defined_in_line": item.lineno,
                    }
                )

        for item in node.body:
            if isinstance(item, ast.ClassDef):
                visit_class(item, [*stack, node.name])

    for stmt in tree.body:
        if isinstance(stmt, ast.ClassDef):
            visit_class(stmt, [])

    return rows


def build_defined_index(src_root: Path) -> dict[str, Any]:
    python_files = sorted(src_root.rglob("*.py"))
    rows: list[dict[str, Any]] = []

    for py_file in python_files:
        rows.extend(_collect_defined_rows_from_file(py_file, src_root))

    method_to_defined_classes: dict[str, list[str]] = {}
    for row in rows:
        method_name = row["method_name"]
        class_id = row["defined_in_class_id"]
        method_to_defined_classes.setdefault(method_name, [])
        if class_id not in method_to_defined_classes[method_name]:
            method_to_defined_classes[method_name].append(class_id)

    for method_name in method_to_defined_classes:
        method_to_defined_classes[method_name] = sorted(method_to_defined_classes[method_name])

    unique_class_ids = {row["defined_in_class_id"] for row in rows}

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_root": str(src_root),
        "file_count": len(python_files),
        "class_count": len(unique_class_ids),
        "method_count": len(method_to_defined_classes),
        "method_to_defined_classes": dict(sorted(method_to_defined_classes.items(), key=lambda kv: kv[0])),
        "rows": sorted(
            rows,
            key=lambda r: (r["method_name"], r["defined_in_module"], r["defined_in_class"], r["defined_in_line"]),
        ),
    }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "method_name",
        "defined_in_class_id",
        "defined_in_class",
        "defined_in_module",
        "defined_in_file",
        "defined_in_line",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in fieldnames})


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan Python classes/methods under src and generate a simple mapping "
            "from method name to classes where the method is directly defined."
        )
    )
    parser.add_argument(
        "--src",
        default=None,
        help="Source root to scan. Default: auto-detected repository src directory.",
    )
    parser.add_argument(
        "--out-json",
        default="artifacts/method_defined_index.json",
        help="Output JSON path. Default: artifacts/method_defined_index.json",
    )
    parser.add_argument(
        "--out-csv",
        default="artifacts/method_defined_index.csv",
        help="Output CSV path. Default: artifacts/method_defined_index.csv",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    default_src_root = Path(__file__).resolve().parents[2]
    src_arg = args.src if args.src else str(default_src_root)
    src_root = Path(src_arg).resolve()

    if not src_root.exists() or not src_root.is_dir():
        print(f"Source directory not found: {src_root}")
        return 1

    payload = build_defined_index(src_root)

    out_json = Path(args.out_json).resolve()
    out_csv = Path(args.out_csv).resolve()
    _write_json(out_json, payload)
    _write_csv(out_csv, payload["rows"])

    print(f"Wrote JSON: {out_json}")
    print(f"Wrote CSV:  {out_csv}")
    print(
        "Summary: "
        f"files={payload['file_count']}, "
        f"classes={payload['class_count']}, "
        f"methods={payload['method_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
