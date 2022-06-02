# External libs
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

# Custom libs
from src.log.logger import Logger


class StartWindowController(QMainWindow):

    def __init__(self):

        Logger.debug("Calling the super class' constructor of StartWindowController")
        super().__init__()
        Logger.info("The super class' constructor of StartWindowController called successfully")

        Logger.debug("Loading start_window.ui")
        self.__start_window = uic.loadUi("..\\..\\Dep\\UI\\start_window.ui")
        Logger.info("Start window loaded successfully (from .ui file)")

        Logger.debug("Setting start window title")
        self.start_window.setWindowTitle("Start Window")
        Logger.info("Start window title set successfully")

        Logger.info("StartWindowController initialized successfully")

    @property
    def start_window(self):
        return self.__start_window
