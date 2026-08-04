# WORK IN PROGRESS: This is just a prelimiary draft of the mcp server for Toolkit

# sir3stoolkit MCP Template

This folder is a package-local template for shipping MCP support with
`sir3stoolkit`.

## Startup configuration

The CLI entrypoint `sir3stoolkit-mcp` can initialize the toolkit at startup.

Options:

- `--sirgraf-dir <PATH>`: use a specific local SirGraf installation path.
- `SIR3S_SIRGRAF_DIR`: environment-variable fallback if `--sirgraf-dir` is not provided.

Examples:

```powershell
sir3stoolkit-mcp --sirgraf-dir "C:\SIR3S\SirGraf-90-15-00-12_Quebec_x64"
```

```powershell
$env:SIR3S_SIRGRAF_DIR = "C:\SIR3S\SirGraf-90-15-00-12_Quebec_x64"
sir3stoolkit-mcp
```

## Included files

- `state.py`: in-memory session state.
- `tools.py`: toolkit-facing tool functions.
- `server.py`: request router and entrypoint placeholder.

## Next steps

1. Choose an MCP framework/transport.
2. Replace `server.py:main` with framework startup code.
3. Add input schemas and stricter validation for each tool.
4. Add tests for happy path and error cases.
