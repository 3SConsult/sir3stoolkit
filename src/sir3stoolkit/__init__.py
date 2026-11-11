"""
sir3stoolkit: Python client for SIR 3S (pipe network simulation/analysis software, 3S Consult).

AI assistant writing code against this package? Quick orientation:
- ``core.wrapper``: thin low-level wrapper around the SIR 3S .NET Toolkit API (``SIR3S_Model``:
  ``OpenModel``, ``GetValue``/``SetValue``, ``ExecCalculation``, ``GetResultValue``, ...).
- ``mantle``: higher-level convenience functions built on core (dataframes, model-editing,
  plotting, alternative-model export) - prefer these when one exists for what you need.
- Docstrings in this package are the ground truth for exact signatures - introspect directly
  (``help(...)``) rather than guessing.
- ``GetValue``/``SetValue``/``GetResultValue`` take opaque property-name strings and OBJTYPE
  codes; see the generated reference at
  https://3sconsult.github.io/sir3stoolkit/object_types_props_results_snippet_global_mapped.html
- Full guide, known gotchas, docs/tutorial links: ``AGENTS.md`` next to this file (its links point at
  this installed version), or https://github.com/3SConsult/sir3stoolkit/blob/main/AGENTS.md (links
  point at the development state on GitHub, which can be ahead of the installed version).
"""

from . import core

__all__ = ['core',
           'mantle',
           ]
