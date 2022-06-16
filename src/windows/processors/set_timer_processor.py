# External libs
from PyQt6.QtWidgets import QLineEdit

# Custom libs
from src.game.game_manager import GameManager
from src.windows.processors.processor import Processor


class SetTimerProcessor(Processor):

    def __init__(self):
        super().__init__("set_timer_window", ok_button=self.ok_button_pressed)

        self.__window = self.manager.get_window("set_timer_window")

        self.timer_period_line_edit = self.__window.findChild(QLineEdit, "timer_period_line_edit")

    def ok_button_pressed(self) -> None:
        period = float(self.timer_period_line_edit.text())
        GameManager.set_timer_period(period)
        self.manager.get_processor("game_window").reset_period()
        self.manager.delete_window(self.window_name)
