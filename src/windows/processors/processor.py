# Built-in libs
from typing import Callable, TYPE_CHECKING

# External libs
from PyQt6.QtWidgets import QPushButton

# Custom libs
from src.log.logger import Logger
from src.windows.renderer import Renderer

if TYPE_CHECKING:
    from src.windows.windows_manager import WindowsManager


class Processor:
    manager: "WindowsManager" = None

    def __init__(self, window_name: str, *args: str, **kwargs: Callable[[], None]):
        self._buttons = {}  # {Button Name: Button Object}
        self._window_name = window_name

        Logger.debug("Calling add_and_connect_button_to_renderer(*args)")
        self.__add_and_connect_button_to_renderer(*args)

        Logger.debug("Calling add_and_connect_button_to_func(**kwargs)")
        self.__add_and_connect_button_to_func(**kwargs)

    @property
    def window_name(self):
        return self._window_name

    @classmethod
    def set_manager(cls, _class) -> None:
        cls.manager = _class

    def __button_exist(self, btn_name: str) -> bool:
        # btn_name is always in buttons.keys(), no need to check.
        return self._buttons[btn_name] is not None

    def __add_and_connect_button_to_func(self, **kwargs: Callable[[], None]) -> None:
        window = self.manager.get_window(self._window_name)

        for btn_name in kwargs:
            self._buttons[btn_name] = window.findChild(QPushButton, btn_name)

            if self.__button_exist(btn_name):
                try:
                    self._buttons[btn_name].clicked.connect(kwargs[btn_name])
                except TypeError:
                    Logger.exception(f"Could not connect {btn_name} to provided function")
            else:
                Logger.info(f"{btn_name} is None")
                del self._buttons[btn_name]

    def __add_and_connect_button_to_renderer(self, *args: str) -> None:

        self.__add_and_connect_button_to_func(
            **{
                btn_name: lambda: Renderer.set_button_action_to_true(self._window_name, f"{btn_name}_pressed")
                for btn_name in args
            }
        )
