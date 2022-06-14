# Built-in libs
from typing import TYPE_CHECKING

# External libs
from PyQt6.QtWidgets import QLabel

# Custom libs
from src import check_time
from src.game.game_manager import GameManager
from src.log.logger import Logger
from src.windows.processors.processor import Processor


class GameWindowProcessor(Processor):
    __btn_to_num = {f"btn_{i}": i for i in range(1, 10)}

    def __init__(self):

        super().__init__(
            "game_window",
            **{f"btn_{i}": self.__x_o_btn_pressed for i in range(1, 10)},
            set_timer_btn=self.__set_timer_btn_pressed,
            start_stop_timer_btn=self.__start_stop_timer_pressed,
            reset_game_btn=self.reset_game,
            reset_round_btn=self.__reset_round,
            leave_btn=self.__leave_btn_pressed
        )

        self.__game_window = self._manager.get_window("game_window")

        self.__player_1_label = self.__game_window.findChild(QLabel, "player_1_label")
        if self.__player_1_label is None:
            Logger.warning("player_1_label is None")

        self.__player_2_label = self.__game_window.findChild(QLabel, "player_2_label")
        if self.__player_2_label is None:
            Logger.warning("player_2_label is None")

    @property
    def game_window(self):
        return self.__game_window

    @check_time
    def __x_o_btn_pressed(self) -> None:
        current_player = GameManager.get_current_player()

        btn = self.__game_window.sender()
        btn.setText(current_player.mark)
        btn.setDisabled(True)

        if current_player.add_a_marked_space(self.__btn_to_num[btn.objectName()]):
            Logger.info(f"{current_player.name} has won")  # Show win window
            current_player.increment_score()
            self.__reset_round()
            return

        if GameManager.tie_check():
            Logger.info("Draw")  # Show draw window
            self.__reset_round()
            return

        GameManager.switch_current_player()
        self.__set_players_labels_color()

    def __set_timer_btn_pressed(self) -> None:
        Logger.info("set_timer_btn_pressed called successfully")

    def __start_stop_timer_pressed(self) -> None:
        Logger.info("start_stop_timer_pressed called successfully")

    def __leave_btn_pressed(self) -> None:
        self.__game_window.close()

        Logger.debug("Calling show for start_window")
        self._manager.get_window("start_window").show()

    def __update_game_window(self) -> None:
        player_1, player_2 = GameManager.get_players()

        self.__player_1_label.setText(f"{player_1.name} ({player_1.mark})\n{player_1.score}")
        self.__player_2_label.setText(f"{player_2.name} ({player_2.mark})\n{player_2.score}")

        self.__set_players_labels_color()

    def __reset_x_o_buttons(self) -> None:
        for i in range(1, 10):
            button = self._buttons[f"btn_{i}"]
            button.setText("")
            button.setEnabled(True)

    def __new_round(self) -> None:
        GameManager.set_marks()
        self.__update_game_window()

    def __reset_round(self) -> None:
        GameManager.reset_marked_spaces()
        GameManager.reset_buttons_pressed()
        self.__reset_x_o_buttons()
        self.__new_round()

    def reset_game(self) -> None:
        GameManager.reset_scores()
        self.__reset_round()

    def __set_players_labels_color(self) -> None:
        if GameManager.get_current_player() is GameManager.get_player_1():
            self.__player_1_label.setStyleSheet("color: red")
            self.__player_2_label.setStyleSheet("color: black")
        else:
            self.__player_1_label.setStyleSheet("color: black")
            self.__player_2_label.setStyleSheet("color: red")
