# Custom libs
from src.windows.controllers.start_window_controller import StartWindowController
from src.windows.processors.start_window_processor import StartWindowProcessor


class WindowsManager:
    __windows = {}

    # @property
    def windows(self) -> dict:
        return self.__windows

    @classmethod
    def set_start_window(cls) -> None:
        WindowsManager.windows["start_window"] = {
            "controller": StartWindowController(),
            "processor": StartWindowProcessor(cls)
        }
