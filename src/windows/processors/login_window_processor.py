# External libs
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QLineEdit

# Custom libs
from src.game.game_manager import GameManager
from src.log.logger import Logger
from src.game.player import Player
from src.windows.processors.processor import Processor
from src.windows.windows_manager import WindowsManager


class LoginWindowProcessor(Processor):

    def __init__(self):
        super().__init__(
            "login_window",
            login_btn=self.login_btn_pressed, cancel_btn=self.cancel_btn_pressed
        )

        self.window = self._windows_manager.get_window(self._window_name)
        self.username_line_edit = self.window.findChild(QLineEdit, "username_line_edit")
        self.password_line_edit = self.window.findChild(QLineEdit, "password_line_edit")

        close = self.window.findChild(QAction, "actionExit")

    def login_btn_pressed(self):
        try:
            Logger.debug("logining")

            username_text = self.username_line_edit.text()
            password_text = self.password_line_edit.text()

            if self.passwordMatch(username_text, password_text):
                if self.window.windowTitle() == "Player 1 Login":
                    GameManager.player_1 = Player(username_text)
                elif self.window.windowTitle() == "Player 2 Login":
                    GameManager.player_2 = Player(password_text)

            self.closeEvent(None)

        except Exception as e:
            Logger.exception(f"Error: {e}")
    def cancel_btn_pressed(self):
        self.closeEvent(None)

    def closeEvent(self, event):
        Logger.debug("closeEvent called")
        self.username_line_edit.setText("")
        self.password_line_edit.setText("")

        self.window.close()

    @staticmethod
    def passwordMatch(username, password):
        return True
