# External libs
from PyQt6.QtWidgets import QPushButton

# Custom libs
from src.log.logger import Logger
from src.windows.renderer import Renderer


class Processor:

    def __init__(self, windows_manager, window_name, *args, **kwargs):
        self.buttons = {}
        self.window_name = window_name
        self.windows_manager = windows_manager
        self.add_and_connect_button_to_renderer(*args)
        self.add_and_connect_button_to_func(**kwargs)

    def button_exist(self, btn_name):
        Logger.debug(f"Checking if {btn_name} is None")
        # btn_name is always in buttons.keys(), no need to check.
        if self.buttons[btn_name] is None:
            Logger.info(f"Did not find {btn_name}")
            return False
        else:
            Logger.info(f"Found {btn_name}")
            return True

    def add_and_connect_button_to_func(self, **kwargs):
        window = self.windows_manager.get_window(self.window_name)

        for btn_name in kwargs:
            Logger.debug(f"Getting {btn_name}")
            self.buttons[btn_name] = window.findChild(QPushButton, btn_name)
            Logger.info(f"{btn_name} accessed successfully (possibly None)")

            Logger.debug(f"Checking if {btn_name} exists")
            if self.button_exist(btn_name):
                Logger.info(f"Found {btn_name}")

                Logger.debug(f"Connecting {btn_name} to the provided function for the button")
                self.buttons[btn_name].clicked.connect(kwargs[btn_name])
                Logger.info(f"Connected {btn_name} to the provided function for the button successfully")
            else:
                Logger.info(f"Did not find {btn_name}")

    def add_and_connect_button_to_renderer(self, *args):

        self.add_and_connect_button_to_func(
            **{
                btn_name: lambda: Renderer.set_button_action_to_true(self.window_name, f"{btn_name}_pressed")
                for btn_name in args
            }
        )
