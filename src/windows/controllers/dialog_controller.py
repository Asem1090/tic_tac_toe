# External libs
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

# Custom libs
from src.log.logger import Logger


class DialogController(QDialog):

    def __init__(self, path: str):
        Logger.debug("Calling the super class' constructor of Controller")
        super().__init__()

        Logger.debug(f"Loading {path}")
        self.__window: QDialog = uic.loadUi(path)

    @property
    def window(self) -> QDialog:
        return self.__window
