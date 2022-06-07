# Built-in libs
from random import randrange
from sys import exit

# Custom libs
from src.log.logger import Logger


class Player:
    # Include rows, columns and both diagonals
    win_lines = frozenset({
        frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9}),  # rows
        frozenset({1, 4, 7}), frozenset({2, 5, 8}), frozenset({3, 6, 9}),  # columns
        frozenset({1, 5, 9}), frozenset({3, 5, 7})  # diagonals
    })

    players_count = 0

    def __new__(cls, *args, **kwargs):
        cls.players_count += 1

    def __init__(self, name: str = f"Player{players_count}"):
        self.__name = name
        self.__score = 0
        self.__mark = None
        self.__marked_spaces = set()

    @property
    def mark(self) -> str:
        return self.__mark

    @classmethod
    def get_possible_win_lines(cls, value: int) -> frozenset[frozenset[int]]:
        lines = set()

        Logger.debug("Iterating through possible win lines")
        for line in cls.win_lines:
            Logger.debug("Checking if value in a win line")
            if value in line:
                Logger.debug("Adding a win line (without the value) to lines")
                lines.add(
                    line.difference(frozenset({value}))
                )
                Logger.info("Added a win line (without the value) to lines successfully")
        Logger.info("Iterated through all lines successfully and returning the win lines as frozenset")
        return frozenset(lines)

    def set_mark(self, other: "Player") -> None:
        Logger.debug("Setting players marks")
        if randrange(1, 201) % 2 == 0:
            self.__mark = 'X'
            other.__mark = 'O'
        else:
            self.__mark = 'O'
            other.__mark = 'X'

    def increment_score(self) -> None:
        self.__score += 1

    def reset_score(self) -> None:
        self.__score = 0

    def add_marked_space(self, value: int) -> bool:
        try:
            if not isinstance(value, int):
                raise AttributeError("Value must be int")
            if value < 1 or value > 9:
                raise ValueError("Value must be a number from 1 to 9")
        except AttributeError or ValueError:
            Logger.exception("Could not add value to marked_spaces")
            exit(1)

        self.__marked_spaces.add(value)

        return self.win_check(value)

    def win_check(self, value: int) -> bool:
        for line in self.get_possible_win_lines(value):
            if line.issubset(self.__marked_spaces):
                return True
