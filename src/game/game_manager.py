# Built-in libs
from random import randrange
from typing import TYPE_CHECKING

# Custom libs
from src.log.logger import Logger

if TYPE_CHECKING:
    from src.game.player import Player


class GameManager:
    # Include rows, columns and both diagonals
    win_lines = frozenset({
        frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9}),  # rows
        frozenset({1, 4, 7}), frozenset({2, 5, 8}), frozenset({3, 6, 9}),  # columns
        frozenset({1, 5, 9}), frozenset({3, 5, 7})  # diagonals
    })

    player_1: "Player" = None
    player_2: "Player" = None

    current_player: "Player" = None

    __btns_pressed = 0

    @classmethod
    def increment_btns_pressed(cls) -> None:
        cls.__btns_pressed += 1

    @classmethod
    def set_marks(cls) -> None:
        Logger.debug("Setting players marks")
        if randrange(1, 201) % 2 == 0:
            cls.player_1.mark = 'X'
            cls.current_player = cls.player_1

            cls.player_2.mark = 'O'
        else:
            cls.player_2.mark = 'X'
            cls.current_player = cls.player_2

            cls.player_1.mark = 'O'

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

    @classmethod
    def win_check(cls, value: int) -> bool:
        for line in cls.get_possible_win_lines(value):
            if line.issubset(GameManager.current_player.marked_spaces):
                return True

    @classmethod
    def switch_current_player(cls) -> None:
        if cls.current_player == cls.player_1:
            cls.current_player = cls.player_2
        elif cls.current_player == cls.player_2:
            cls.current_player = cls.player_1

    @classmethod
    def draw_check(cls) -> bool:
        return cls.__btns_pressed == 9

