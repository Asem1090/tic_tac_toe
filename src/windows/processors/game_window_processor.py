# Built-in libs
from typing import TYPE_CHECKING

# Custom libs
from src.log.logger import Logger
from src.windows.processors.processor import Processor

if TYPE_CHECKING:
    from src.windows.windows_manager import WindowsManager


class GameWindowProcessor(Processor):

    def __init__(self, windows_manager: "WindowsManager"):
        player_1 = None
        player_2 = None

        super().__init__(
            windows_manager, "game_window",
            **{f"btn_{i}": self.x_o_btn_pressed for i in range(1, 10)},
            **{"set_timer_btn": self.set_timer_btn_pressed,
               "start_stop_timer_btn": self.start_stop_timer_pressed,
               "reset_game_btn": self.reset_game_btn_pressed,
               "reset_round_btn": self.reset_round_btn_pressed,
               "leave_btn": self.leave_btn_pressed}
        )

    def x_o_btn_pressed(self) -> None:
        btn = self.windows_manager.get_window(self.window_name).sender()
        btn.setText("X")
        btn.setDisabled(True)
        Logger.info("x_o_btn_pressed called successfully")

    def set_timer_btn_pressed(self) -> None:
        Logger.info("set_timer_btn_pressed called successfully")

    def start_stop_timer_pressed(self) -> None:
        Logger.info("start_stop_timer_pressed called successfully")

    def reset_game_btn_pressed(self) -> None:
        Logger.info("reset_game_btn_pressed called successfully")

    def reset_round_btn_pressed(self) -> None:
        Logger.info("reset_round_btn_pressed called successfully")

    def leave_btn_pressed(self) -> None:
        Logger.info("leave_btn_pressed called successfully")
