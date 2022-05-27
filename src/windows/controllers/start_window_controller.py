# External libs
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class StartWindowController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.__start_window = uic.loadUi("..\\..\\Dep\\UI\\start_window.ui")

        self.start_window.setWindowTitle("Start Window")

    @property
    def start_window(self):
        return self.__start_window
