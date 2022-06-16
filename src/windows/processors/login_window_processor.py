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
            login_btn=self.__login_btn_pressed, cancel_btn=self.__cancel_btn_pressed
        )

        self.window = self.__manager.get_window(self.__window_name)
        self.username_line_edit = self.window.findChild(QLineEdit, "username_line_edit")
        self.password_line_edit = self.window.findChild(QLineEdit, "password_line_edit")

        # close = self.window.findChild(QAction, "actionExit")

    def __login_btn_pressed(self) -> None:
        username_text = self.username_line_edit.text()
        password_text = self.password_line_edit.text()

        window_title = self.window.windowTitle()

        if self.__password_match(username_text, password_text):
            if window_title == "Player 1 Login":
                GameManager.set_player_1(username_text)
            elif window_title == "Player 2 Login":
                GameManager.set_player_2(username_text)

        self.__close_event()

    def __cancel_btn_pressed(self) -> None:
        self.__close_event()

    def __close_event(self) -> None:
        self.username_line_edit.setText("")
        self.password_line_edit.setText("")

        self.window.close()

    @staticmethod
    def __password_match(username, password) -> bool:
        return True
