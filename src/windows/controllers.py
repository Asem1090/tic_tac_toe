# External libs
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QDialog

# Custom libs
from log.logger import Logger


class MainWindowController(QMainWindow):

    def __init__(self, path: str):
        Logger.debug("Calling the super class' constructor of Controller")
        super().__init__()

        Logger.debug(f"Loading {path}")
        self.__window: QMainWindow = uic.loadUi(path)  # TODO PUT SELF OR OTHER CLASS!

    @property
    def window(self) -> QMainWindow:
        return self.__window


class DialogController(QDialog):

    def __init__(self, path: str):
        Logger.debug("Calling the super class' constructor of Controller")
        super().__init__()

        Logger.debug(f"Loading {path}")
        self.__window: QDialog = uic.loadUi(path)  # TODO PUT SELF OR OTHER CLASS!

    @property
    def window(self) -> QDialog:
        return self.__window
