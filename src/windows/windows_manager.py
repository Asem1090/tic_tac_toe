# Custom libs
from src.log.logger import Logger
from src.windows.controllers.start_window_controller import StartWindowController
from src.windows.processors.start_window_processor import StartWindowProcessor


class WindowsManager:
    __windows = {}

    @classmethod
    @property
    def windows(cls):
        return WindowsManager.__windows

    @staticmethod
    def set_start_window() -> None:
        Logger.debug("Creating start window controller and processor objects")

        WindowsManager.windows["start_window"] = {}

        Logger.debug("Creating StartWindowController object and storing it in __windows")
        WindowsManager.windows["start_window"]["controller"] = StartWindowController()
        Logger.info("StartWindowController stored in __windows successfully")

        Logger.debug("Creating StartWindowProcessor object and storing it in __windows")
        WindowsManager.windows["start_window"]["processor"] = StartWindowProcessor(WindowsManager)
        Logger.info("StartWindowProcessor object stored in __windows successfully")
