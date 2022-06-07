# External libs
from PyQt6.QtWidgets import QLineEdit

# Custom libs
from src.log.logger import Logger
from src.miscellaneous.player import Player
from src.windows.processors.processor import Processor
from src.windows.windows_manager import WindowsManager


class LoginWindowProcessor(Processor):

    def __init__(self, windows_manager: WindowsManager):
        super().__init__(
            windows_manager, "login_window",
            login_btn=self.login_btn_pressed, cancel_btn=self.cancel_btn_pressed
        )

    def login_btn_pressed(self):
        Logger.debug("logining")

        window = self._windows_manager.get_window(self._window_name)
        username = window.findChild(QLineEdit, "username_line_edit")
        password = window.findChild(QLineEdit, "password_line_edit")

        if self.passwordMatch(username, password):
            Player(username.text())

        self._windows_manager.get_window(self._window_name).close()

    def cancel_btn_pressed(self):
        self._windows_manager.get_window(self._window_name).close()

    @staticmethod
    def passwordMatch(username, password):
        return True