# Built-in libs
from sys import exit
from typing import Type, TypeVar

# External libs
from PyQt6.QtWidgets import QMainWindow

# Custom libs
from src.log.logger import Logger
from src.windows.controllers.dialog_controller import DialogController
from src.windows.controllers.main_window_controller import MainWindowController
from src.windows.processors.processor import Processor

processor_subclass = TypeVar("processor_subclass", bound=Type[Processor])


class WindowsManager:
    __windows = {}

    @classmethod
    def __get_controller(cls, window_name: str) -> MainWindowController:
        Logger.debug(f"Getting {window_name} controller")
        window_controller: MainWindowController = cls.__windows[window_name]["controller"]
        Logger.info(f"{window_name} controller accessed successfully")

        try:
            if window_controller is None:
                raise AttributeError(f"WindowsManager.__windows[{window_name}][\"controller\"] is None")

        except AttributeError:
            Logger.exception(f"{window_name} controller is None")
            exit(-1)

        return window_controller

    @classmethod
    def get_window(cls, window_name: str) -> QMainWindow:
        Logger.debug(f"Getting {window_name} from {window_name} controller")
        window = cls.__get_controller(window_name).window
        Logger.info(f"{window_name} accessed successfully from {window_name} controller")

        Logger.info(f"Returning {window_name}")
        return window

    @classmethod
    def set_window(
            cls, window_name: str, processor: processor_subclass,
            window_type: str = "QMainWindow", ui_file_path: str = None
    ) -> None:

        if window_name in cls.__windows.keys():
            Logger.info("Window already exists")
            return

        Logger.debug(f"Creating {window_name} controller and processor objects")

        cls.__windows[window_name] = {}

        if ui_file_path is None:
            ui_file_path = f"..\\..\\Dep\\UI\\{window_name}.ui"

        if window_type == "QMainWindow":
            Logger.debug("Creating MainWindowController object")
            cls.__windows[window_name]["controller"] = MainWindowController(ui_file_path)
            Logger.info("Created MainWindowController object successfully")
        elif window_type == "QDialog":
            Logger.debug("Creating MainWindowController object")
            cls.__windows[window_name]["controller"] = DialogController(ui_file_path)
            Logger.info("Created MainWindowController object successfully")
        else:
            Logger.warning("WRONG WINDOW TYPE!")
            return

        Logger.debug(f"Creating {window_name} processor object")
        cls.__windows[window_name]["processor"] = processor(cls)
        Logger.info(f"Created {window_name} processor object successfully")

