# External libs
from PyQt6.QtWidgets import QApplication

# Custom libs
from src.windows.windows_manager import WindowsManager


class MainClass:

    def __init__(self):

        self.__app = QApplication([])

        windows_manager = WindowsManager()
        windows_manager.set_start_window()

        windows_manager.start_window_controller.start_window.show()

    def run(self):

        try:
            exit(self.__app.exec())

        except SystemExit as E:
            print(f"Exiting the System:\n{E}")
