# External libs
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

# Custom libs
from src.log.logger import Logger


class Controller(QMainWindow):

    def __init__(self, path: str):
        Logger.debug("Calling the super class' constructor of Controller")
        super().__init__()
        Logger.info("The super class' constructor of Controller called successfully")

        Logger.debug(f"Loading {path}")
        self.__window: QMainWindow = uic.loadUi(path)
        Logger.info(f"{path} loaded successfully")

    @property
    def window(self) -> QMainWindow:
        return self.__window
