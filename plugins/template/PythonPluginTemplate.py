# This file is part of PythonPluginTemplate.

"""
Python Plugin Template.

Author: Michael Fischer
"""

# General modules
import clr
import ctypes
import logging
from pathlib import Path
from PySide6 import QtWidgets, QtCore
import os
import sys
import weakref

logging.basicConfig(
    filename='log_app.txt',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Package modules
logging.info("Import user_gui.")

import user_gui

logging.info("Import resources.")
import resources

# Entry points
plugin_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, plugin_dir)  # Caution: path[0] is reserved for script path

logging.info("Entry point plugin_dir: " + plugin_dir)

logging.info("Resolve SirGraf directory.")

sir3s_path = resources.resolve_sirgraf_dir(explicit=None,
                                           plugin_dir=Path(plugin_dir),
                                           validate=True)
sirgraf_dir = str(sir3s_path)

logging.info("Successfully resolved SirGraf directory:" + sirgraf_dir)

# Init SIR 3S

# Init dlls for Plugin interface
sys.path.append(sirgraf_dir)

clr.AddReference(r"System")
clr.AddReference(sirgraf_dir + "\\Sir3S_Repository.ModelManager")
clr.AddReference(sirgraf_dir + "\\Sir3S_Repository.Utilities")
clr.AddReference(sirgraf_dir + "\\Sir3S_Repository.Interfaces")

from System.Collections.Generic import List  # noqa: 402
import Sir3S_Repository.Utilities as Utils  # noqa: 402
import Sir3S_Repository.Interfaces as Interfaces  # noqa: 402
import Sir3S_Repository.ObjectModel.Interfaces as ObjectInterfaces  # noqa: 402

logging.info("Import all DLLs as libs successfully.")

# App singletons
_app_owner = False
_main_windows = weakref.WeakSet()


def ensure_qapp():
    """Create or reuse the single QApplication. Never start the loop here."""
    global _app_owner
    app = QtWidgets.QApplication.instance()
    if app is None:
        # Wichtig: Setze Attribute vor Erstellung (DPI/OpenGL sind optional, aber hilfreich)
        QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
        app = QtWidgets.QApplication(sys.argv)
        _app_owner = True
    return app


def show_window_nonblocking(w: QtWidgets.QWidget):
    """Show window non-blocking in foreground without starting event loop."""

    _main_windows.add(w)  # weak reference - deleted automatically when window is closed
    w.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    w.show()
    w.raise_()
    w.activateWindow()



# Definition of CPluginTemplate interface from SIRGraf
# (SIR3S application can invoke this plugin)
class CPluginTemplate(Interfaces.IPlugin):

    __namespace__ = "PluginNameSpace_PythonPluginTemplate"  # Important, needs to be unique!

    def Name(self):
        return "PythonPluginTemplate"

    def Description(self):
        return "PythonPluginTemplate"

    def WpfUI(self):
        logging.info("WpfUI called.")
        return None

    def WinFormsUI(self):
        logging.info("WinFormsUI called.")
        return None

    def ClickedElement(self, element: ObjectInterfaces.IElementBase,
                       linear_projection: Interfaces.IPoint3D) -> bool:
        logging.info("ClickedElement called.")
        return True

    def ExecuteCommand(self, command: Interfaces.IPluginCommand):
        logging.info("ExecuteCommand called.")
        return Utils.CRepositoryResult(Interfaces.ModelBridgeResult.OK, "")

    def GetErrorMessage(self, error_code: int) -> str:
        logging.error(f"GetErrorMessage called with error_code: {error_code}")
        return ""

    def GetToolTipText(self, element: ObjectInterfaces.IElementBase):
        logging.info(f"GetToolTipText called with element: {element}")
        return List[str]()

    def Init(self, object_model: ObjectInterfaces.IObjectModel,
             presenter: Interfaces.IPresenter):
        self._object_model = object_model
        self._presenter = presenter

        try:   # GUI execution

            logging.info("Start GUI execution.")

            # COM init: in Hostumgebungen ist CoInitialize evtl. schon gesetzt
            # Sicherer ist: ignorieren, wenn schon initialisiert
            try:
                ctypes.windll.ole32.CoInitializeEx(None, 0x2)  # apartment-threaded
            except Exception:
                pass

            # App cycle
            logging.info("Start App cycle.")

            app = ensure_qapp()

            # WICHTIG: starke Referenz am Plugin-Objekt halten
            if getattr(self, "_window", None) is None or self._window is None:
                self._window = user_gui.UserMainWindow()
                # Wenn das Fenster zerstört wird, Owner-Referenz wieder freigeben
                self._window.destroyed.connect(lambda *_: setattr(self, "_window", None))

            # show_window_nonblocking(window)
            show_window_nonblocking(self._window)
            logging.info("Window shown (non-blocking).")
            logging.info("End GUI execution.")

        except Exception as ex:
            print(f"Error: {ex}")
            logging.error(f"Error: {ex}")
            return 2

        return 0

    def Release(self):
        logging.info("Release called.")
        pass
