# Built-in libs
from typing import Callable, TYPE_CHECKING

# External libs
from PyQt6.QtWidgets import QPushButton

# Custom libs
from src.log.logger import Logger
from src.windows.renderer import Renderer

if TYPE_CHECKING:
    from src.windows.windows_manager import WindowsManager


class Processor:

    def __init__(self, windows_manager: "WindowsManager", window_name: str, *args: str, **kwargs: Callable):
        self.buttons = {}
        self.window_name = window_name
        self.windows_manager = windows_manager

        Logger.debug("Calling add_and_connect_button_to_renderer(*args)")
        self.add_and_connect_button_to_renderer(*args)
        Logger.info("Called add_and_connect_button_to_renderer(*args) successfully")

        Logger.debug("Calling add_and_connect_button_to_func(**kwargs)")
        self.add_and_connect_button_to_func(**kwargs)
        Logger.info("Called add_and_connect_button_to_func(**kwargs) successfully")

    def button_exist(self, btn_name: str) -> bool:
        Logger.debug(f"Checking if {btn_name} is None")
        # btn_name is always in buttons.keys(), no need to check.
        if self.buttons[btn_name] is None:
            Logger.info(f"Did not find {btn_name}")
            return False
        else:
            Logger.info(f"Found {btn_name}")
            return True

    def add_and_connect_button_to_func(self, **kwargs: Callable) -> None:
        window = self.windows_manager.get_window(self.window_name)

        for btn_name in kwargs:
            Logger.debug(f"Getting {btn_name}")
            self.buttons[btn_name] = window.findChild(QPushButton, btn_name)
            Logger.info(f"{btn_name} accessed successfully (possibly None)")

            Logger.debug(f"Checking if {btn_name} exists")
            if self.button_exist(btn_name):
                Logger.info(f"{btn_name} exists (not None)")

                Logger.debug(f"Connecting {btn_name} to the provided function for the button")
                self.buttons[btn_name].clicked.connect(kwargs[btn_name])
                Logger.info(f"Connected {btn_name} to the provided function for the button successfully")
            else:
                Logger.info(f"{btn_name} is None")

                Logger.debug(f"Deleting {btn_name} from buttons")
                self.buttons.pop(btn_name)
                Logger.info(f"Deleted {btn_name} from buttons")

    def add_and_connect_button_to_renderer(self, *args: str) -> None:

        self.add_and_connect_button_to_func(
            **{
                btn_name: lambda: Renderer.set_button_action_to_true(self.window_name, f"{btn_name}_pressed")
                for btn_name in args
            }
        )
