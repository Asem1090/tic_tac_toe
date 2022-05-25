# Custom libs
from src.windows.controllers.start_window_controller import StartWindowController
from src.windows.processors.start_window_processor import StartWindowProcessor


class WindowsManager:
    __start_window_controller = None
    __start_window_processor = None

    @property
    def start_window_controller(self):
        return WindowsManager.__start_window_controller

    @property
    def start_window_processor(self):
        return WindowsManager.__start_window_processor

    def set_start_window(self):
        WindowsManager.start_window_controller = StartWindowController(self)
        WindowsManager.start_window_processor = StartWindowProcessor(self)
