# Built-in libs
from sys import exit

# External libs
from PyQt6.QtWidgets import QPushButton

# Custom libs
from src.log.logger import Logger
from src.windows.renderer import Renderer


class StartWindowProcessor:

    def __init__(self, windows_manager):
        self.buttons = {}
        self.window_name = "start_window"

        # Accessing start window controller
        Logger.debug(f"Getting {self.window_name} controller from WindowsManager")
        window_controller = windows_manager.windows[self.window_name]["controller"]
        Logger.info(f"{self.window_name} controller accessed successfully from WindowsManager")

        try:
            if window_controller is None:
                raise AttributeError(f"WindowsManager.windows[{self.window_name}][\"controller\"] is None")

        except AttributeError:
            Logger.exception(f"{self.window_name} controller is None")
            exit(-1)

        # Accessing start window
        Logger.debug(f"Getting {self.window_name} from {self.window_name} controller")
        self.window = window_controller.start_window
        Logger.info(f"{self.window_name} accessed successfully from {self.window_name} controller")

        # Accessing the buttons and connecting them to self.change.
        Logger.debug("Calling add_and_connect_button for pvp_btn")
        self.add_and_connect_button("pvp_btn")
        Logger.info("Called add_and_connect_button for pvp_btn")

        Logger.debug("Calling add_and_connect_button for pve_btn")
        self.add_and_connect_button("pve_btn")
        Logger.info("Called add_and_connect_button for pve_btn")

        Logger.debug("Calling add_and_connect_button for local_network_btn")
        self.add_and_connect_button("local_network_btn")
        Logger.info("Called add_and_connect_button for local_network_btn")

    def button_exist(self, btn_name):
        Logger.debug(f"Checking if found {btn_name}")
        # btn_name is always in self.buttons.keys(), no need to check.
        if self.buttons[btn_name] is None:
            Logger.info(f"Did not find {btn_name}")
            return False
        else:
            Logger.info(f"Found {btn_name}")
            return True

    def add_and_connect_button(self, btn_name):
        # Accessing btn_name
        Logger.debug(f"Getting {btn_name}")
        self.buttons[btn_name] = self.window.findChild(QPushButton, btn_name)
        Logger.info(f"{btn_name} accessed successfully (possibly None)")

        Logger.debug(f"Checking if {btn_name} exists")
        if self.button_exist(btn_name):
            Logger.info(f"Found {btn_name}")

            Logger.debug(f"Connecting {btn_name} to lambda function")
            self.buttons[btn_name].clicked.connect(
                lambda: Renderer.set_button_action_to_true(self.window_name, btn_name)
            )
            Logger.info(f"Connected {btn_name} to lambda function successfully")
        else:
            Logger.info(f"Did not find {btn_name}")

    def pvp_btn_pressed(self):
        pass

    def pve_btn_pressed(self):
        pass

    def local_network_btn_pressed(self):
        pass
