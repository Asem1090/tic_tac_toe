# External libs
from PyQt6.QtWidgets import QApplication

# Custom libs
from src.log.logger import Logger
from src.windows.renderer import Renderer
from src.windows.windows_manager import WindowsManager


class MainClass:

    def __init__(self):

        Logger.debug("Creating QApplication object")
        self.__app = QApplication([])
        Logger.info("QApplication object created successfully")

        Logger.debug("Calling set_start_window from WindowsManager")
        WindowsManager.set_start_window()

        Logger.debug("Calling show for start window")
        WindowsManager.windows["start_window"]["controller"].start_window.show()
        Logger.info("Show called successfully for start window")

        Logger.debug("Calling start from Renderer")
        Renderer.start()

        Logger.info("MainClass initialized successfully")

    def run(self):

        try:
            Logger.info("Executing the application / Displaying start window")
            exit_code = self.__app.exec()
            Logger.info("Application execution complete")

            exit(exit_code)

        except SystemExit as E:
            Logger.exception("Exiting the system")
