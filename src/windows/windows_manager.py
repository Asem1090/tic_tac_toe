# Custom libs
from src.windows.controllers.start_window_controller import StartWindowController
from src.windows.processors.start_window_processor import StartWindowProcessor


class WindowsManager:
    windows = {}

    @property
    def start_window_controller(self):
        return WindowsManager.__start_window_controller

    @property
    def start_window_processor(self):
        return WindowsManager.__start_window_processor

    @classmethod
    def set_start_window(cls):
        WindowsManager.windows["start_window"] = {}
        WindowsManager.windows["start_window"]["controller"] = StartWindowController()
        WindowsManager.windows["start_window"]["processor"] = StartWindowProcessor(cls)
