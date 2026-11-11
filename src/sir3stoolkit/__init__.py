"""
sir3stoolkit: Python client for SIR 3S (pipe network simulation/analysis software, 3S Consult).

AI assistant writing code against this package? Read the guide for AI assistants of the installed
version first: ``AGENTS.md`` next to this file (links pointing at this version; more files, incl. the
code of every tutorial as plain text, in ``ai/`` next to it). Initialize_Toolkit() logs its path.
Without the installed package: https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/AGENTS.md
(development state on GitHub, which can be ahead of the released version). Quick orientation until then:
- ``core.wrapper``: thin low-level wrapper around the SIR 3S .NET Toolkit API (``SIR3S_Model``:
  ``OpenModel``, ``GetValue``/``SetValue``, ``ExecCalculation``, ``GetResultValue``, ...).
- ``mantle``: higher-level convenience functions built on core (dataframes, model-editing,
  plotting, alternative-model export) - prefer these when one exists for what you need.
- Docstrings in this package are the ground truth for exact signatures - introspect directly
  (``help(...)``) rather than guessing.
- ``GetValue``/``SetValue``/``GetResultValue`` take opaque property-name strings and OBJTYPE
  codes; see the generated reference at
  https://3sconsult.github.io/sir3stoolkit/object_types_props_results_snippet_global_mapped_with_descriptions.html
  - the same reference ships with the package: ``SIR3S_Model_Dataframes.get_object_type_reference()``
  looks up one element type without an open model (``mantle/object_type_reference.json`` for all).
"""

from . import core

__all__ = ['core',
           'mantle',
           ]
