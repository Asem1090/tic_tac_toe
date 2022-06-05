# Built-in libs
from sys import exit

# Custom libs
from src.log.logger import Logger
from src.windows.controller import Controller


# External libs


class WindowsManager:
    __windows = {}

    @classmethod
    @property
    def windows(cls):
        return WindowsManager.__windows

    @staticmethod
    def get_window(window_name) -> Controller:
        # Accessing controller
        Logger.debug(f"Getting {window_name} controller")
        window_controller = WindowsManager.windows[window_name]["controller"]
        Logger.info(f"{window_name} controller accessed successfully")

        try:
            if window_controller is None:
                raise AttributeError(f"WindowsManager.windows[{window_name}][\"controller\"] is None")

        except AttributeError:
            Logger.exception(f"{window_name} controller is None")
            exit(-1)

        # Accessing start window
        Logger.debug(f"Getting {window_name} from {window_name} controller")
        window = window_controller.window
        Logger.info(f"{window_name} accessed successfully from {window_name} controller")

        Logger.info(f"Returning {window_name}")
        return window

    @staticmethod
    def set_window(window_name, ui_file_path, processor) -> None:
        Logger.debug(f"Creating {window_name} controller and processor objects")

        WindowsManager.windows[window_name] = {}

        Logger.debug("Creating Controller object")
        WindowsManager.windows[window_name]["controller"] = Controller(ui_file_path)
        Logger.info("Created Controller object successfully")

        Logger.debug(f"Creating {window_name} processor object")
        WindowsManager.windows[window_name]["processor"] = processor(WindowsManager)
        Logger.info(f"Created {window_name} processor object successfully")

