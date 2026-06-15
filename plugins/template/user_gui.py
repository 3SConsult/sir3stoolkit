# This file is part of PythonPluginTemplate.

"""
Graphical user interface module.

Author: Michael Fischer
"""

# General modules
from PySide6 import QtWidgets

# Package modules
import ui


class UserMainWindow(QtWidgets.QMainWindow):
    """GUI: Main window."""

    def __init__(self, parent=None):

        # Ui
        super().__init__(parent)

        self.ui = ui.ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # Program name
        self.setWindowTitle("Python Plugin Template")
