# Built-in libs
from typing import Type, TypeVar, Union

# External libs
from PyQt6.QtWidgets import QMainWindow

# Custom libs
from src.log.logger import Logger
from src.windows.controllers.dialog_controller import DialogController
from src.windows.controllers.main_window_controller import MainWindowController
from src.windows.processors.processor import Processor

processor_subclass = TypeVar("processor_subclass", bound=Type[Processor])
controller = Union[MainWindowController, DialogController]


class WindowsManager:
    __windows = {}

    @classmethod
    def __get_controller(cls, window_name: str) -> controller:
        Logger.info(f"Accessing and returning {window_name} controller")
        return cls.__windows[window_name]["controller"]

    @classmethod
    def get_processor(cls, window_name: str) -> processor_subclass:
        Logger.info(f"Accessing and returning {window_name} processor")
        return cls.__windows[window_name]["processor"]

    @classmethod
    def get_window(cls, window_name: str) -> QMainWindow:
        Logger.info(f"Accessing {window_name} from {window_name} controller and returning it")
        return cls.__get_controller(window_name).window

    @classmethod
    def set_window(
            cls, window_name: str, processor: processor_subclass,
            window_type: str = "QMainWindow", ui_file_path: str = None
    ) -> None:

        if cls.window_exists(window_name):
            return

        if ui_file_path is None:
            ui_file_path = f"..\\..\\Dep\\UI\\{window_name}.ui"

        windows = cls.__windows

        if window_type == "QMainWindow":
            windows[window_name] = {}
            Logger.debug("Creating MainWindowController object")
            windows[window_name]["controller"] = MainWindowController(ui_file_path)

        elif window_type == "QDialog":
            windows[window_name] = {}
            Logger.debug("Creating DialogController object")
            windows[window_name]["controller"] = DialogController(ui_file_path)
        else:
            Logger.warning("WRONG WINDOW TYPE!")
            return

        Logger.debug(f"Creating {window_name} processor object")
        windows[window_name]["processor"] = processor()

    @classmethod
    def window_exists(cls, window_name: str) -> bool:
        if window_name in cls.__windows.keys():
            Logger.info("Window exists")
            return True
        Logger.warning("Window does not exist")
        return False
