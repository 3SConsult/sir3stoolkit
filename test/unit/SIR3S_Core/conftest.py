"""
conftest.py used at parent folder test/ helps to mock the .NET behaviour and tests the
functionalities without the help of real SIR3S. This works fine for functionalities entirely written in python
like mantle.

But for wrapper and graph, it will be useful to call the real SIR3S installation and test the wrapping methods.
This conftest.py file helps to organize all the necessary fixtures needed for a real interaction between python 
and .NET. This also means it might be relatively slower because of the need to load necessary dlls and calls to 
.NET
"""

import os
import pytest

SIRGRAF_DIR = os.environ.get(
    "SIR3S_SIRGRAF_DIR",
    r"C:\Users\giriyan\Work_Content\SIR3S\SirGraf-90-15-00-24_Quebec-Upd2",
)


@pytest.fixture(scope="session")
def sir3s_real():
    """Initialize real SIR 3S once, or skip all tests that need it."""
    if not os.path.isdir(SIRGRAF_DIR):
        pytest.skip(f"SirGraf folder not found: {SIRGRAF_DIR}")
    try:
        from sir3stoolkit.core.wrapper import Initialize_Toolkit
        Initialize_Toolkit(SIRGRAF_DIR)
    except Exception as exc:
        pytest.skip(f"SIR 3S could not be initialized: {exc}")