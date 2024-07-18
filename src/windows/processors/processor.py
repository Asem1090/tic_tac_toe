# Built-in libs
from typing import Callable, TYPE_CHECKING, Type

# External libs
from PyQt6.QtWidgets import QPushButton

# Custom libs
from log.logger import Logger

if TYPE_CHECKING:
    from windows.windows_manager import WindowsManager


class Processor:
    __manager: Type["WindowsManager"] = None

    def __init__(self, window_name: str, **kwargs: Callable[[], None]):
        self._buttons = {}  # {Button Name: Button Object}
        self.__window_name = window_name

        Logger.debug("Calling add_and_connect_button_to_func(**kwargs)")
        self.__add_and_connect_button_to_func(**kwargs)

    @property
    def manager(self) -> Type["WindowsManager"]:
        return Processor.__manager

    @property
    def window_name(self) -> str:
        return self.__window_name

    @window_name.setter
    def window_name(self, value: str) -> None:
        if not Processor.__manager.window_exists(value):
            Logger.warning(f"This window '{value}' does not exist yet.")

        self.__window_name = value

    @classmethod
    def set_manager(cls, manager: Type["WindowsManager"]) -> None:
        cls.__manager = manager

    def __button_exist(self, btn_name: str) -> bool:
        # btn_name is always in buttons.keys(), no need to check.
        return self._buttons[btn_name] is not None

    def __add_and_connect_button_to_func(self, **kwargs: Callable[[], None]) -> None:
        window = Processor.__manager.get_window(self.__window_name)

        for btn_name in kwargs:
            self._buttons[btn_name] = window.findChild(QPushButton, btn_name)

            if self.__button_exist(btn_name):
                try:
                    self._buttons[btn_name].clicked.connect(kwargs[btn_name])
                except TypeError:
                    Logger.exception(
                        f"Could not connect {btn_name} to provided function"
                    )
            else:
                Logger.info(f"{btn_name} is None")
                del self._buttons[btn_name]
