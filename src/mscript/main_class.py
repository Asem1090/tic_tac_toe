# Built-in libs
import time
from sys import exit

# External libs
from PyQt6.QtWidgets import QApplication

# Custom libs
from src.game.game_manager import GameManager
from src.game.player import Player
from src.log.logger import Logger
from src.windows.processors.processor import Processor
from src.windows.processors.start_window_processor import StartWindowProcessor
from src.windows.windows_manager import WindowsManager


class MainClass:

    def __init__(self):
        self.set_values()

        Logger.debug("Creating QApplication object")
        self.__app = QApplication([])
        Logger.info("QApplication object created successfully")

        WindowsManager.set_window("start_window", StartWindowProcessor)

        Logger.debug("Calling show for start window")
        WindowsManager.get_window("start_window").show()
        Logger.info("show called successfully for start window")

    @staticmethod
    def set_values():
        Player.game_manager = GameManager
        Processor._windows_manager = WindowsManager

    def run(self) -> None:

        try:
            Logger.info("Executing the application / Displaying start window")
            exit_code = self.__app.exec()

            exit(exit_code)

        except SystemExit as E:
            Logger.threadless_debug(f"Exiting the system: {E}")
