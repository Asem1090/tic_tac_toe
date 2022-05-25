from PyQt6.QtWidgets import QPushButton


class StartWindowProcessor:

    def __init__(self, windows_manager):
        window_controller = windows_manager.start_window_controller

        if window_controller is None:
            raise AttributeError("ControllersManager.start_window_controller is None")

        self.__x_o_buttons = \
            {f"b{i}": window_controller.start_window.findChild(QPushButton, f"b{i}") for i in range(1, 10)}

