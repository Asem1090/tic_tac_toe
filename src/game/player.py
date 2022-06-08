# Built-in libs
from sys import exit
from typing import Literal

# Custom libs
from src.game.game_manager import GameManager
from src.log.logger import Logger


class Player:

    def __init__(self, name: str):
        self.__name = name
        self.__score = 0
        self.__mark = None
        self.__marked_spaces = set()

    @property
    def name(self):
        return self.__name

    @property
    def mark(self) -> str:
        return self.__mark

    @property
    def marked_spaces(self) -> set[int]:
        return self.__marked_spaces

    @mark.setter
    def mark(self, value: Literal['X', 'O']) -> None:
        try:
            if value != 'X' and value != 'O':
                raise ValueError(f"Cannot set mark to {value}. Value must be 'X' or 'O'.")
        except ValueError:
            Logger.exception("Error in setting value for mark")

        self.__mark = value

    def increment_score(self) -> None:
        self.__score += 1

    def reset_score(self) -> None:
        self.__score = 0

    def add_marked_space(self, value: int) -> bool:
        Logger.debug("add_marked")  # Fix
        try:
            if not isinstance(value, int):
                raise AttributeError("Value must be int")
            if value < 1 or value > 9:
                raise ValueError("Value must be a number from 1 to 9")
        except AttributeError or ValueError:
            Logger.exception("Could not add value to marked_spaces")
            exit(1)

        self.__marked_spaces.add(value)
        GameManager.increment_btns_pressed()

        return GameManager.win_check(value)
