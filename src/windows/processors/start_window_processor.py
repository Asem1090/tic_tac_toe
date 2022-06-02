# External libs
from PyQt6.QtWidgets import QPushButton

# Custom libs
from src.log.logger import Logger


class StartWindowProcessor:

    def __init__(self, windows_manager):
        Logger.debug("Getting start window controller from WindowsManager")
        window_controller = windows_manager.windows["start_window"]["controller"]
        Logger.info("Start window controller accessed successfully from WindowsManager")

        if window_controller is None:
            Logger.exception("Start window controller does not exist")
            raise AttributeError("WindowsManager.windows[\"start_window\"][\"controller\"] is None")

        Logger.debug("Getting start_window from start window controller")
        window = window_controller.start_window
        Logger.info("start_window accessed successfully from start window controller")

        Logger.debug("Getting the pvp_btn")
        self.pvp_btn = window.findChild(QPushButton, "pvp_btn")
        Logger.info("pvp_btn accessed successfully")

        Logger.debug("Getting the pve_btn")
        self.pve_btn = window.findChild(QPushButton, "pve_btn")
        Logger.info("pve_btn accessed successfully")

        Logger.debug("Getting the local_network_btn")
        self.local_network_btn = window.findChild(QPushButton, "local_network_btn")
        Logger.info("local_network_btn accessed successfully")

        Logger.info("StartWindowProcessor initialized successfully")

    def pvp_btn_pressed(self):
        pass

    def pve_btn_pressed(self):
        pass

    def local_network_btn_pressed(self):
        pass
