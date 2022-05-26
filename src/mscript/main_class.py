# External libs
from PyQt6.QtWidgets import QApplication

# Custom libs
from src.windows.windows_manager import WindowsManager


class MainClass:

    def __init__(self):

        self.__app = QApplication([])

        WindowsManager.set_start_window()

        WindowsManager.windows["start_window"]["controller"].start_window.show()

    def run(self):

        try:
            exit(self.__app.exec())

        except SystemExit as E:
            print(f"Exiting the System:\n{E}")
