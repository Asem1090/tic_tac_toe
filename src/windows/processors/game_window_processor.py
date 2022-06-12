# Built-in libs
from typing import TYPE_CHECKING

# External libs
from PyQt6.QtWidgets import QLabel

# Custom libs
from src.game.game_manager import GameManager
from src.log.logger import Logger
from src.windows.processors.processor import Processor

if TYPE_CHECKING:
    from src.windows.windows_manager import WindowsManager


class GameWindowProcessor(Processor):
    btn_to_num = {f"btn_{i}": i for i in range(1, 10)}

    def __init__(self):

        super().__init__(
            "game_window",
            **{f"btn_{i}": self.x_o_btn_pressed for i in range(1, 10)},
            set_timer_btn=self.set_timer_btn_pressed,
            start_stop_timer_btn=self.start_stop_timer_pressed,
            reset_game_btn=self.reset_game_btn_pressed,
            reset_round_btn=self.reset_round_btn_pressed,
            leave_btn=self.leave_btn_pressed
        )

        self.game_window = self._windows_manager.get_window("game_window")

        self.player_1_label = self.game_window.findChild(QLabel, "player_1_label")
        if self.player_1_label is None:
            Logger.warning("player_1_label is None")

        self.player_2_label = self.game_window.findChild(QLabel, "player_2_label")
        if self.player_2_label is None:
            Logger.warning("player_2_label is None")

    def x_o_btn_pressed(self) -> None:
        current_player = GameManager.current_player

        btn = self.game_window.sender()
        btn.setText(current_player.mark)
        btn.setDisabled(True)

        if current_player.add_marked_space(self.btn_to_num[btn.objectName()]):
            Logger.info(f"{current_player.name} has won")  # Show win window

        if GameManager.tie_check():
            Logger.info("Draw")  # Show draw window

        GameManager.switch_current_player()

    def set_timer_btn_pressed(self) -> None:
        Logger.info("set_timer_btn_pressed called successfully")

    def start_stop_timer_pressed(self) -> None:
        Logger.info("start_stop_timer_pressed called successfully")

    def reset_game_btn_pressed(self) -> None:
        Logger.info("reset_game_btn_pressed called successfully")

    def reset_round_btn_pressed(self) -> None:
        Logger.info("reset_round_btn_pressed called successfully")

    def leave_btn_pressed(self) -> None:
        Logger.debug("Closing game_window")
        self.game_window.close()

        Logger.debug("Calling show for start_window")
        self._windows_manager.get_window("start_window").show()

    def show_game_window(self):
        player_1 = GameManager.player_1
        player_2 = GameManager.player_2

        GameManager.set_marks()

        self.player_1_label.setText(f"{player_1.name} ({player_1.mark})\n{player_1.score}")
        self.player_2_label.setText(f"{player_2.name} ({player_2.mark})\n{player_2.score}")

        self.game_window.show()
