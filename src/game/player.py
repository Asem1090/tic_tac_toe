# Built-in libs
from typing import Literal, TYPE_CHECKING, Type

# Custom libs
from src.log.logger import Logger

if TYPE_CHECKING:
    from src.game.game_manager import GameManager


class Player:
    __manager: Type["GameManager"] = None

    def __init__(self, name: str):
        self.__name = name
        self.__score = 0
        self.__mark = None
        self.__marked_spaces = set()

    @property
    def manager(self) -> Type["GameManager"]:
        return Player.__manager

    @property
    def name(self) -> str:
        return self.__name

    @property
    def score(self) -> int:
        return self.__score

    @property
    def mark(self) -> str:
        return self.__mark

    @property
    def marked_spaces(self) -> set[int]:
        return self.__marked_spaces

    @mark.setter
    def mark(self, value: Literal['X', 'O']) -> None:
        if value not in frozenset({'X', 'O'}):
            Logger.error(f"Cannot set mark to {value}. Value must be 'X' or 'O'.")

        self.__mark = value

    @classmethod
    def set_manager(cls, _class) -> None:
        cls.__manager = _class

    def increment_score(self) -> None:
        self.__score += 1

    def add_a_marked_space(self, value: int) -> bool:
        if not (isinstance(value, int) or value in range(1, 10)):
            Logger.error(f"Got unexpected value: {value!r}")
            return False

        self.__marked_spaces.add(value)
        self.__manager.increment_buttons_pressed()
        return self.__manager.win_check(value)

    def reset_score(self) -> None:
        self.__score = 0

    def reset_marked_spaces(self) -> None:
        self.__marked_spaces.clear()
