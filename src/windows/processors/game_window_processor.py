# External libs
from typing import NewType, Union

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QLabel, QMainWindow

# Custom libs
from src.game.game_manager import GameManager
from src.log.logger import Logger
from src.windows.processors.processor import Processor
from src.windows.processors.set_timer_processor import SetTimerProcessor

UPDATE_PERIOD = 0.1
MILLISECOND_UPDATE_PERIOD: int = int(UPDATE_PERIOD * 1000)

POSITIVE_INTEGER = NewType("POSITIVE_INTEGER", int)


class GameWindowProcessor(Processor):
    __btn_to_num = {f"btn_{i}": i for i in range(1, 10)}

    def __init__(self):
        self.__period: Union[int, float] = 5
        self.__is_timer_on = False

        super().__init__(
            "game_window",
            **{f"btn_{i}": self.__x_o_btn_pressed for i in range(1, 10)},
            set_timer_btn=self.__set_timer_btn_pressed,
            start_stop_timer_button=self.__start_stop_timer_button_pressed,
            reset_game_btn=self.reset_game,
            reset_round_btn=self.__reset_round,
            leave_btn=self.__leave_btn_pressed
        )

        self.__game_window = self.__manager.get_window("game_window")

        self.__player_1_label = self.__game_window.findChild(QLabel, "player_1_label")
        if self.__player_1_label is None:
            Logger.warning("player_1_label is None")

        self.__player_2_label = self.__game_window.findChild(QLabel, "player_2_label")
        if self.__player_2_label is None:
            Logger.warning("player_2_label is None")

        self.__timer_label = self.__game_window.findChild(QLabel, "timer_label")

        self.__qtimer = QTimer()
        self.__qtimer.timeout.connect(self.__update)

    @property
    def game_window(self) -> QMainWindow:
        return self.__game_window

    @property
    def period(self) -> Union[int, float]:
        return self.__period

    @period.setter
    def period(self, value: POSITIVE_INTEGER) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            Logger.warning(f"Value must be a positive integer, got {value!r}")

        self.__period = value

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

        self.__period = self.__period = GameManager.get_timer_period()
        GameManager.switch_current_player()
        self.__set_players_labels_color()

    def __set_timer_btn_pressed(self) -> None:
        self.__manager.set_window("set_timer_window", SetTimerProcessor)
        self.__manager.get_window("set_timer_window").show()

    def __start_timer(self) -> None:
        self.__timer_label.setText(f"{self.__period:.1f}")
        self.__qtimer.start(MILLISECOND_UPDATE_PERIOD)

    def __update(self) -> None:
        self.__period -= UPDATE_PERIOD

        if self.__period > 0:
            self.__timer_label.setText(f"{self.__period:.1f}")
        else:
            self.__period = GameManager.get_timer_period()
            self.__timer_label.setText(f"{self.__period:.1f}")
            self.__timeout()

    def __timeout(self) -> None:
        GameManager.switch_current_player()
        self.__set_players_labels_color()

    def __stop_timer(self) -> None:
        self.__qtimer.stop()

    def __start_stop_timer_button_pressed(self) -> None:
        if self.__is_timer_on:
            self.__is_timer_on = False
            self.__stop_timer()
        else:
            self.__is_timer_on = True
            self.__start_timer()

    def __leave_btn_pressed(self) -> None:
        self.__game_window.close()

        Logger.debug("Calling show for start_window")
        self.__manager.get_window("start_window").show()

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
        self.__period = self.__period = GameManager.get_timer_period()
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
