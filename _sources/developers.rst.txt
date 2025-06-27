For Developers
==============

Welcome to the Developers page! This section provides resources and instructions for developers who want to contribute to Sir3SToolkit-Documentation. 

- **Toolkit Contact**: If you encounter an issue with the Toolkit that should be fixed or have an idea for enhancement, feel free to create an new entry on our `GitHub forum <https://github.com/3SConsult/sir3stoolkit/issues>`_. Please include the Toolkit and SirGraf version you are using and, if available, the Jupyter Notebook you are working with.

- **Documentation Contact**: For additional information regarding this documentation, and contribution inquiries, please contact `jablonski@3sconsult.de <mailto:jablonski@3sconsult.de>`_.

- **GitHub Repository:** `GitHub Repository <https://github.com/3SConsult/sir3stoolkit>`_.

- **PyPI Page:** `PyPI Page <https://pypi.org/project/sir3stoolkit/>`_.

Setting Up Git on Your Computer
-------------------------------

Follow these steps to install and configure Git:

1. **Download Git:** Visit the `official Git website <https://git-scm.com/downloads>`_ and download the version that is compatible with your operating system.

2. **Install Git:** Launch the downloaded installer and follow the setup wizard to complete the installation.

3. **Configure Your GitHub Username:** Open your terminal or command prompt and enter the following command, replacing "Your Name" with your actual GitHub username:

   .. code-block:: bash

      git config --global user.name "Your Name"

4. **Configure Your GitHub Email:** Similarly, set your GitHub email using the following command, replacing ``your.email@example.com`` with your actual email:

   .. code-block:: bash

      git config --global user.email "your.email@example.com"

.. note::

   If you're pushing your first commit to GitHub, you might be prompted to authenticate your GitHub account. This usually involves entering your GitHub account credentials in a browser dialogue window that pops up. This is a standard security measure to ensure you have the necessary permissions to push to the repository.

Working with GitHub
-------------------

.. _cloning-github-label: 

Cloning the GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To clone a GitHub repository to your local folder, follow these steps:

1. **Navigate to the Parent Directory of Your Project:** Use the ``cd`` command followed by the path to the parent directory of your project (This is the directory that should contain your project folder).

   .. code-block:: bash

      cd "C:\Users\User\3S"

2. **Clone the GitHub Repository:** Use the ``git clone`` command followed by the URL of the repository.

   .. code-block:: bash

      git clone https://github.com/3SConsult/sir3stoolkit


General GitHub Version Control Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These instructions lay out the different steps of the GitHub procedure around contributing to Sir3SToolkit-Documentation. Especially due to the GitHub repository currentley sitting on only one branch (master), following these basic rules is crucial. As soon as Sir3SToolkit-Documentation has a higher amount of frequent contributors, a more suitable system with multiple branches will be implemented.

.. note::
    Before following each step for the first time, read their instructions fully including notes like this one. If an unexpected problem occurs, you can search the :ref:`command-collection-label` for a solution.

Follow these steps every time you contribute to Sir3SToolkit-Documentation:

1. **Get the Latest Version from GitHub**: :ref:`get-latest-version-label`

2. **Edit Sir3SToolkit-Documentation**: Now you can edit the entire Sir3SToolkit-Documentation project locally. Please ensure, that nobody else is working on the project simultaneously in the same sourcefiles, because this could cause problems, when trying to commit.

3. **Commit Your Changes to the GitHub Repository**: :ref:`commit-changes-label`

.. _get-latest-version-label:

Get the Latest Version from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fetch the latest changes from the origin and merge them into your current branch, follow these steps:

1. **Navigate to project directory:** Use the ``cd`` command followed by the path to the directory of your project (This directory should contain an invisible .git folder).

   .. code-block:: bash

      cd "C:\Users\User\3S\Sir3SToolkit-Documentation"
      
2. **Pull the latest changes from the origin**: Use the ``git pull`` command. 

   .. code-block:: bash

      git pull origin master
        
   For a more detailed updating process, follow steps 2 and 3 instead.
        
2. **Fetch the latest changes from the origin:** Use the ``git fetch origin`` command.

   .. code-block:: bash

      git fetch origin

3. **Merge the fetched changes into your current branch:** Use the ``git merge origin/master`` command.

   .. code-block:: bash

      git merge origin/master

.. note::
    If you made local changes to files that were also edited by a remote commit, make a local copy of your project directory and use ``git reset --hard origin/master``. Afterwards you can paste you local changes back in. Just make sure that the remote changes to these files were not important or manually include them in your files.

.. code-block:: bash

   git reset --hard origin/master  

.. _commit-changes-label:

Commit Your Changes to the GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To commit your changes to the GitHub repository, follow these steps:

1. **Navigate to project directory:** Use the ``cd`` command followed by the path to the directory of your project (This directory should contain an invisible .git folder).

   .. code-block:: bash

      cd "C:\Users\User\3S\Sir3SToolkit-Documentation"

2. **Add files to the staging area:** Use the ``git add`` command followed by the name of the file. Use ``git add .`` to add all files.

   .. code-block:: bash

      git add .

3. **Create a new commit with a descriptive message:** Use the ``git commit -m "commit_message"`` command.

   .. code-block:: bash

      git commit -m "commit_message"

4. **Push your commit to the GitHub Repository:** Use the ``git push origin master`` command.

   .. code-block:: bash

      git push origin master

.. .. note::
    If you want to push multiple commits back to back, keep in mind that the Sir3SToolkit-Documentation GitHub repository uses :ref:`github-workflow-label` that might require you to fetch after committing to certain directories. Because workflows can automatically author commits, so fetching ensures you have the latest changes. Alternatively you can check the :ref:`current-workflow-label` utilised by the GitHub Repository and whether the might be triggered by your commit.

.. _command-collection-label:

Collection of Useful Git Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To discard all local changes and set your local HEAD to the master, use:

   .. code-block:: bash

      git reset --hard origin/master

To discard all remote changes and force push local HEAD to the master, use:

   .. code-block:: bash

      git push origin master --force
           
To uncommit commited but not yet pushed changes of the previous commit without changing local files (move HEAD pointer back by one commit), use:

   .. code-block:: bash

      git reset --soft HEAD~1

To revert all changes caused by a commit, use:

   .. code-block:: bash

      git revert commitID
      
To load a branch locally, use:

   .. code-block:: bash

      git checkout <branchname>

.. _github-workflow-label:

GitHub Workflows
~~~~~~~~~~~~~~~~

.. note:: This section has to be adjusted for new Repository.

Our GitHub repository uses workflows to facilitate certain processes by automating tasks. Workflows are defined using YAML files and are stored in the `.github/workflows` directory of our repository.

.. _current-workflow-label:

Current Workflows
^^^^^^^^^^^^^^^^^

All of our workflows can be triggered using :ref:`manually-triggering-workflows-label`. 

We currently use the following workflows:

.. list-table:: 
   :header-rows: 1

   * - **Name**
     - **Triggers (Apart from manually triggering)**
     - **Tasks**
   * - Automatic Copying of HTML-Files
     - Push to `Sir3SToolkit-Documentation/build/html/`
     - Copies HTML files from master `Sir3SToolkit-Documentation/build/html` to gh-pages `Sir3SToolkit-Documentation/docs`

.. _manually-triggering-workflows-label:

Manually Triggering Workflows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow these steps to manually trigger a workflow via GitHub:

1. Navigate to the **Actions** tab of the Sir3SToolkit-Documentation GitHub repository.

2. Select the workflow you want to trigger from the list on the left.

3. Click the **Run workflow** button.

4. Optionally, provide any required inputs and click **Run workflow** again to start the workflow.
     
Generating the Documentation
----------------------------

.. note:: This section has to be adjusted for new Repository.

The Toolkit documentation is edited in Sir3SToolkit-Documentation/source on the master branch and files hosting the documentation are located in Sir3SToolkit-Documentation/build/html on the master branch and in Sir3SToolkit-Documentation/docs on the gh-pages branch

If you want to edit the documentation yourself, you have to install sphinx and sphinx related python packages.

   .. code-block:: bash

      pip install sphinx nbsphinx sphinx_copybutton sphinx-rtd-theme sphinx-togglebutton

To generate documentation, follow these steps:

1. **Edit the documentation:** Make your changes on the rst files in the Sir3SToolkit-Documentation/source.

2. **Navigate to the Sir3SToolkit-Documentation directory:** Use the ``cd`` command.

   .. code-block:: bash

      cd "C:\Users\User\3S\Sir3SToolkit-Documentation"

3. **Make an HTML build:** Use ``python3 -m sphinx.cmd.build -b html . /_build/html`` (for python env)  or ``.\make.bat html`` (for conda env (recommended to use conda shell)).

   .. code-block:: bash

      python3 -m sphinx.cmd.build -b html . /_build/html
   
   .. code-block:: bash

      .\make.bat html

.. 3. **Use Build File**: Alternatively, instead of using the ``.\make.bat html`` command, you can simply open the `Toolkit/sphinx_docs/make_html_docs.py` file and run it to generate the documentation. This method will not print any Sphinx debugging output and will save time. This alternative is recommended when making many iterative improvements to the documentation.

4. **Commit the changes.** Commit all files from Sir3SToolkit-Documentation to GitHub (:ref:`commit-changes-label`).

.. 5. **Get the Latest Version**: You should :ref:`get-latest-version-label` before continuing to edit local.

The new documentation can be found at `https://mj3s.github.io/Sir3SToolkit-Documentation/index.html <https://mj3s.github.io/Sir3SToolkit-Documentation/index.html#>`_

.. note::

   The created files in Sir3SToolkit/build/html on the master branch are moved to Sir3SToolkit/docs on the gh-pages branch by one of our :ref:`github-workflow-label` and then hosted via GitHubPages. It might take a couple of minutes until the changes are visible on the website.