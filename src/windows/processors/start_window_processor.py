from PyQt6.QtWidgets import QPushButton


class StartWindowProcessor:

    def __init__(self, windows_manager):
        window_controller = windows_manager.windows["start_window"]["controller"]

        if window_controller is None:
            raise AttributeError("ControllersManager.start_window_controller is None")

        window = window_controller.start_window

        self.pvp_btn = window.findChild(QPushButton, "pvp_btn")
        self.pve_btn = window.findChild(QPushButton, "pve_btn")
        self.local_network_btn = window.findChild(QPushButton, "local_network_btn")

    def pvp_btn_pressed(self):
        pass

    def pve_btn_pressed(self):
        pass

    def local_network_btn_pressed(self):
        pass
