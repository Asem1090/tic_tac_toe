"""
This file contains the main script.
"""

# Built-in libs
from sys import exit

# External libs
from PyQt6.QtWidgets import QApplication

# Custom libs
from game.game_manager import GameManager
from game.player import Player
from log.logger import Logger
from windows.processors.processor import Processor
from windows.processors.start_window_processor import StartWindowProcessor
from windows.windows_manager import WindowsManager


class MainClass:
    """
    The main script is here, for better structure.
    """

    def __init__(self):
        """
        We create some required variables here then call show method for a window.
        """

        self.__set_managers()

        Logger.debug("Creating QApplication object")
        self.__app = QApplication([])
        Logger.info("QApplication object created successfully")

        WindowsManager.set_window("start_window", StartWindowProcessor)

        Logger.debug("Calling show for start window")
        WindowsManager.get_window("start_window").show()
        Logger.info("show called successfully for start window")

    @staticmethod
    def __set_managers() -> None:
        """
        Setting managers here to avoid circular import.
        :return: None
        """
        Player.set_manager(GameManager)
        Processor.set_manager(WindowsManager)

    def run(self) -> None:
        """
        The application is executed here.
        :return: None
        """

        try:
            Logger.info("Executing the application / Displaying start window")
            exit_code = self.__app.exec()

            exit(exit_code)

        except SystemExit as E:
            Logger.threadless_debug(f"Exiting the system: {E}")
