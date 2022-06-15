from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QWidget

from src import Logger


class SignalManager(QObject):
    signal = pyqtSignal(str)

    def signal_func(self, func, var):
        try:
            self.signal.connect(func)
            self.signal.emit(var)
        except Exception as e:
            Logger.exception(e)