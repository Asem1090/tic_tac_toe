# External libs
from PyQt6.QtWidgets import QLineEdit

# Custom libs
from src import Logger
from src.game.game_manager import GameManager
from src.windows.processors.processor import Processor


class SetTimerProcessor(Processor):

    def __init__(self):
        super().__init__("set_timer_window", ok_button=self.ok_button_pressed)

        self.window = self._manager.get_window("set_timer_window")

        self.timer_period_line_edit = self.window.findChild(QLineEdit, "timer_period_line_edit")

    def ok_button_pressed(self):
        Logger.info("ok_button_pressed called successfully")
        GameManager.set_timer_period(float(self.timer_period_line_edit.text()))
        self.window.destroy()
        Logger.info("ok_button_pressed called successfully")
