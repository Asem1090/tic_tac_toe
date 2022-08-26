# Built-in libs
from typing import Type, TypeVar, Union

# External libs
from PyQt6.QtWidgets import QMainWindow

# Custom libs
from src.log.logger import Logger
from src.windows.controllers import DialogController
from src.windows.controllers import MainWindowController
from src.windows.processors.processor import Processor

PROCESSOR_SUBCLASS = TypeVar("PROCESSOR_SUBCLASS", bound=Type[Processor])
CONTROLLER = Union[MainWindowController, DialogController]


class WindowsManager:
    __windows = {}  # { window_name: {"controller": CONTROLLER, "processor" PROCESSOR_SUBCLASS}, ... }

    @classmethod
    def get_controller(cls, window_name: str) -> CONTROLLER:
        Logger.info(f"Accessing and returning {window_name} controller")
        return cls.__windows[window_name]["controller"]

    @classmethod
    def get_processor(cls, window_name: str) -> PROCESSOR_SUBCLASS:
        Logger.info(f"Accessing and returning {window_name} processor")
        return cls.__windows[window_name]["processor"]

    @classmethod
    def get_window(cls, window_name: str) -> QMainWindow:
        Logger.info(f"Accessing {window_name} from {window_name} controller and returning it")
        return cls.get_controller(window_name).window

    @classmethod
    def set_window(
            cls, window_name: str, processor: PROCESSOR_SUBCLASS,
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
    def delete_window(cls, window_name: str) -> bool:
        if not cls.window_exists(window_name):
            return False

        del cls.__windows[window_name]
        return True

    @classmethod
    def window_exists(cls, window_name: str) -> bool:
        return window_name in cls.__windows.keys()
