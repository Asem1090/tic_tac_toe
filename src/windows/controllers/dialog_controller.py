# External libs
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

# Custom libs
from src.log.logger import Logger


class DialogController(QDialog):

    def __init__(self, path: str):
        Logger.debug("Calling the super class' constructor of Controller")
        super().__init__()
        Logger.info("The super class' constructor of Controller called successfully")

        Logger.debug(f"Loading {path}")
        self.__window: QDialog = uic.loadUi(path)
        Logger.info(f"{path} loaded successfully")

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    @property
    def window(self) -> QDialog:
        return self.__window
