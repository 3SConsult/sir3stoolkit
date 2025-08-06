Releases
========

The SIR 3S Toolkit will first be released alongside SIR 3S version 90-15 Quebec, under the version 90.15.2. 
Between major SIR 3S releases, the Toolkit may receive interim updates to fix bugs or extend functionality.

There are two types of updates:

1. **Python-only updates** – Install via:

   .. code-block:: bash

      pip install --upgrade sir3stoolkit

2. **Core updates with DLL changes** – Requires manual replacement of ``Sir3S_Toolkit.dll`` in the SirGraf directory **before** running the upgrade.


This can either be a pure python update that can be obtained using ``pip install --upgrade sir3stoolkit`` or 
it can include changes in the basic functionality code wrapped by the core subpackage. 
In this case before upgrading via pip the ``Sir3S_Toolkit.dll`` in the SirGraf directory has to be exchanged. 
The release notes indicate what kind of release it is.

90-15 Quebec
------------

Version 90.15.2 (Initial Release)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- First official public release of the SIR 3S Toolkit
- Introduced core wrapping API for SIR 3S object model (nodes, pipes, etc.)
- Compatible with SIR 3S 90-15 Quebec (requires Sir3S_Toolkit.dll)
- Included example workflows and basic simulation access
