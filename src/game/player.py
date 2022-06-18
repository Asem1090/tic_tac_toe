"""
This file defines Player, and its attributes and behaviors.
"""

# Built-in libs.
from typing import Literal, TYPE_CHECKING, Type, Optional

# Custom libs.
from src.log.logger import Logger

if TYPE_CHECKING:  # Prevents circular import when type hinting.
    from src.game.game_manager import GameManager


class Player:
    """
    This class defines each player's attributes and methods.
    """

    __manager: Type["GameManager"] = None

    def __init__(self, name: str):
        """
        Sets Player.__name and defines some default private attributes.
        :param name: A string, represents the name of the player.
        """

        self.__name = name
        self.__score = 0
        self.__mark: Optional[Literal['X', 'O']] = None  # Either X or O.
        self.__marked_spaces = set()  # 1-9, represents the positions of the marks the player has.

    @property
    def manager(self) -> Type["GameManager"]:
        """
        A getter for Player.__manager.
        :return: Player.__manager, which should be GameManager.
        """

        return Player.__manager

    @property
    def name(self) -> str:
        """
        A getter for Player.__name.
        :return: A string, represents the player's name.
        """

        return self.__name

    @property
    def score(self) -> int:
        """
        A getter for Player.__score.
        :return: A positive int, represents the player's score.
        """

        return self.__score

    @property
    def mark(self) -> str:
        """
        A getter for Player.__mark.
        :return: Either 'X' or 'O', represents the player's mark.
        """

        return self.__mark

    @property
    def marked_spaces(self) -> set[int]:
        """
        A getter for Player.__marked_spaces.
        :return: A set of integers (1-9), represents all spaces the player has marked.
        """

        return self.__marked_spaces

    @mark.setter
    def mark(self, value: Literal['X', 'O']) -> None:
        """
        A setter for Player.__mark.
        :param value: A string, should be X or O.
        :return: None
        """

        # Checking whether value is X or O, or something else.
        if value not in frozenset({'X', 'O'}):
            Logger.error(f"Cannot set mark to {value}, value must be 'X' or 'O'.")
            return

        self.__mark = value

    @classmethod
    def set_manager(cls, _class) -> None:
        """
        A setter for Player.__manager.
        :param _class: A class, should GameManager.
        :return: None
        """

        cls.__manager = _class

    def increment_score(self) -> None:
        """
        Increments Player.__score by 1.
        :return: None
        """

        self.__score += 1

    def add_a_marked_space(self, value: int) -> Optional[bool]:
        """
        Adds value to Player.__marked_spaces (only if value is 1-9), and does win/tie related processes.
        :param value: A integer (1-9), represents the position of the marked space.
        :return: True if the player has won, False if not, and None if value is not 1-9.
        """

        # Checking if value is not 1-9.
        if not (isinstance(value, int) or value in range(1, 10)):
            Logger.error(f"Got unexpected value: {value!r}")
            return

        self.__marked_spaces.add(value)
        self.__manager.increment_buttons_pressed()
        return self.__manager.win_check(value)

    def reset_score(self) -> None:
        """
        Sets Player.__score to 0.
        :return: None
        """

        self.__score = 0

    def reset_marked_spaces(self) -> None:
        """
        Removes all items in Player.__marked_spaces.
        :return: None
        """

        self.__marked_spaces.clear()
