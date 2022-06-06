# Built-in libs
from sys import exit
from typing import Type, TypeVar

# External libs
from PyQt6.QtWidgets import QWidget

# Custom libs
from src.log.logger import Logger
from src.windows.controller import Controller
from src.windows.processors.processor import Processor

processor_subclass = TypeVar("processor_subclass", bound=Type[Processor])


class WindowsManager:
    __windows = {}

    @staticmethod
    def __get_controller(window_name: str) -> Controller:
        Logger.debug(f"Getting {window_name} controller")
        window_controller: Controller = WindowsManager.__windows[window_name]["controller"]
        Logger.info(f"{window_name} controller accessed successfully")

        try:
            if window_controller is None:
                raise AttributeError(f"WindowsManager.__windows[{window_name}][\"controller\"] is None")

        except AttributeError:
            Logger.exception(f"{window_name} controller is None")
            exit(-1)

        return window_controller

    @staticmethod
    def get_window(window_name: str) -> QWidget:
        Logger.debug(f"Getting {window_name} from {window_name} controller")
        window = WindowsManager.__get_controller(window_name).window
        Logger.info(f"{window_name} accessed successfully from {window_name} controller")

        Logger.info(f"Returning {window_name}")
        return window

    @staticmethod
    def set_window(window_name: str, ui_file_path: str, processor: processor_subclass) -> None:
        Logger.debug(f"Creating {window_name} controller and processor objects")

        WindowsManager.__windows[window_name] = {}

        Logger.debug("Creating Controller object")
        WindowsManager.__windows[window_name]["controller"] = Controller(ui_file_path)
        Logger.info("Created Controller object successfully")

        Logger.debug(f"Creating {window_name} processor object")
        WindowsManager.__windows[window_name]["processor"] = processor(WindowsManager)
        Logger.info(f"Created {window_name} processor object successfully")

