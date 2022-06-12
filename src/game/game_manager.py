# Built-in libs
from random import randrange
from typing import Generator

from src.game.player import Player


class GameManager:
    # Includes rows, columns and both diagonals
    win_lines = frozenset({
        frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9}),  # rows
        frozenset({1, 4, 7}), frozenset({2, 5, 8}), frozenset({3, 6, 9}),  # columns
        frozenset({1, 5, 9}), frozenset({3, 5, 7})  # diagonals
    })

    player_1 = Player("Player 1")
    player_2 = Player("Player 2")

    current_player = None

    __buttons_pressed = 0

    @classmethod
    def increment_buttons_pressed(cls) -> None:
        cls.__buttons_pressed += 1

    @classmethod
    def set_marks(cls) -> None:
        if randrange(1, 201) & 1:
            cls.player_1.mark = 'X'
            cls.player_2.mark = 'O'

            cls.current_player = cls.player_1
        else:
            cls.player_1.mark = 'O'
            cls.player_2.mark = 'X'

            cls.current_player = cls.player_2

    @classmethod
    def switch_current_player(cls) -> None:
        cls.current_player = cls.player_1 \
            if (cls.current_player is cls.player_2)\
            else cls.player_2

    # CHECK SPEED FROZENSET OR SET
    @classmethod
    def get_possible_win_lines(cls, value: int) -> Generator[frozenset[int]]:
        for line in cls.win_lines:
            if value in line:
                yield line.difference({value})

    @classmethod
    def win_check(cls, value: int) -> bool:
        for line in cls.get_possible_win_lines(value):
            if line.issubset(GameManager.current_player.marked_spaces):
                return True
        return False

    @classmethod
    def tie_check(cls) -> bool:
        return cls.__buttons_pressed == 9
