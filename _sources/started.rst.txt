Getting Started
===============

.. note::
    This documentation is still WORK IN PROGRESS.

Welcome to the Getting Started guide for the SIR 3S Toolkit! This guide is your first step towards understanding and utilizing the Toolkit. The purpose of the Toolkit and its applications will be explained.

Why is the Toolkit valuable when Working with SIR 3S
----------------------------------------------------

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

**The SIR 3S Toolkit is only of interest to users with access to SIR 3S models.**

.. _installing-toolkit-label: 

Get SIR 3S Version with Toolkit Compatibility
---------------------------------------------

Follow these steps:

1. **Get SIR 3S Version with Python Compatibility**: Copy ``S:/Softwareentwicklung/SIR 3S/Sir3S-90/Release_Intern/2024-11-26_Release_Quebec(Alpha)/SirCalc-90-15-00-12_Quebec.alpha_x64.zip`` and ``S:/Softwareentwicklung/SIR 3S/Sir3S-90/Release_Intern/2024-11-26_Release_Quebec(Alpha)/SirGraf-90-15-00-06x64.ZIP`` to your local machine preferably to ``C:/3S/SIR 3S Entwicklung``.

2. **Unpack .zip files**: Unpack both zip-folders.

3. **Get Common folder with Python for new SIR 3S Version**: Copy ``S:/Softwareentwicklung/SIR 3S/Sir3S-90/Common`` to your local machine preferably to ``C:/3S/SIR 3S Entwicklung``.

4. **Unpack .zip files**: Unpack the python zip folder in the Common folder. Make sure that ``C:/3S/SIR 3S Entwicklung/Common/Python312/python.exe`` exists.

5. **Get License for SIR 3S 90**: Copy ``SIR3S-90.LIC`` from ``T:/SCRATCH/Jablonski`` to ``C:/3S/SIR 3S Entwicklung/Common``.

6. **Upgrade pip and install numpy**: Open a cmd and enter the following commands:

   .. code-block:: bash

       cd "C:/3S/SIR 3S Entwicklung/SirGraf-90-15-00-06x64/Python312"
       #python.exe -m pip install --upgrade pip (if needed)
       python.exe -m pip install numpy

Install Toolkit
---------------

To install the Toolkit, follow these steps:

1. **Install Toolkit via pip in SIR 3S Environment:** Open a cmd and enter the following commands:

   .. code-block:: bash

       cd "C:/3S/SIR 3S Entwicklung/Common/Python312"
       python.exe -m pip install sir3stoolkit


2. **Install Toolkit via pip in other Environment:** Open a cmd in the desired environment and enter the following commands:

   .. code-block:: bash

       pip install sir3stoolkit
       
If you encounter issues with that, located the python.exe file of the environment and follow step 1.

We now invite you to visit the :doc:`examples` page to understand basic Toolkit functionalities.
