# Built-in libs
from sys import exit

# External libs
from PyQt6.QtWidgets import QApplication

# Custom libs
from src.game.game_manager import GameManager
from src.game.player import Player
from src.log.logger import Logger
from src.windows.processors.start_window_processor import StartWindowProcessor
from src.windows.windows_manager import WindowsManager


class MainClass:

    def __init__(self):
        # Setting default players
        GameManager.player_1 = Player("Player 1")
        GameManager.player_2 = Player("Player 2")

        Logger.debug("Creating QApplication object")
        self.__app = QApplication([])
        Logger.info("QApplication object created successfully")

        Logger.debug("Calling set_window from WindowsManager")
        WindowsManager.set_window("start_window", StartWindowProcessor)

        Logger.debug("Calling show for start window")
        WindowsManager.get_window("start_window").show()
        Logger.info("show called successfully for start window")

    def run(self) -> None:

        try:
            Logger.info("Executing the application / Displaying start window")
            exit_code = self.__app.exec()

            exit(exit_code)

        except SystemExit:
            Logger.exception("Exiting the system")
