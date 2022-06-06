# Built-in libs
from sys import exit

# External libs
from PyQt6.QtWidgets import QApplication

# Custom libs
from src.log.logger import Logger
from src.windows.processors.start_window_processor import StartWindowProcessor
from src.windows.renderer import Renderer
from src.windows.windows_manager import WindowsManager


class MainClass:

    def __init__(self):
        Logger.debug("Initializing MainClass object")

        Logger.debug("Creating QApplication object")
        self.__app = QApplication([])
        Logger.info("QApplication object created successfully")

        Logger.debug("Calling set_window from WindowsManager")
        WindowsManager.set_window("start_window", "..\\..\\Dep\\UI\\start_window.ui", StartWindowProcessor)

        Logger.debug("Calling show for start window")
        WindowsManager.get_window("start_window").show()
        Logger.info("show called successfully for start window")

        Logger.info("MainClass initialized successfully")

    def run(self) -> None:

        try:
            Logger.info("Executing the application / Displaying start window")
            exit_code = self.__app.exec()
            Logger.info("Application execution complete")

            exit(exit_code)

        except SystemExit:
            Logger.exception("Exiting the system")
