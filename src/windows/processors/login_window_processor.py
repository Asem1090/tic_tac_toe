# External libs
from PyQt6.QtWidgets import QLineEdit

# Custom libs
from src.game.game_manager import GameManager
from src.game.player import Player
from src.windows.processors.processor import Processor


class LoginWindowProcessor(Processor):

    def __init__(self):
        super().__init__(
            "login_window",
            login_btn=self.login_btn_pressed, cancel_btn=self.cancel_btn_pressed
        )

        self.window = self._windows_manager.get_window(self._window_name)
        self.username_line_edit = self.window.findChild(QLineEdit, "username_line_edit")
        self.password_line_edit = self.window.findChild(QLineEdit, "password_line_edit")

        # close = self.window.findChild(QAction, "actionExit")

    def login_btn_pressed(self):
        username_text = self.username_line_edit.text()
        password_text = self.password_line_edit.text()

        window_title = self.window.windowTitle()

        if self.password_match(username_text, password_text):
            if window_title == "Player 1 Login":
                GameManager.player_1 = Player(username_text)
            elif window_title == "Player 2 Login":
                GameManager.player_2 = Player(username_text)

        self.close_event()


    def cancel_btn_pressed(self):
        self.close_event()

    def close_event(self):
        self.username_line_edit.setText("")
        self.password_line_edit.setText("")

        self.window.close()

    @staticmethod
    def password_match(username, password):
        return True
