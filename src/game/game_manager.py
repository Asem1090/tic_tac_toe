# Built-in libs
from random import randrange
from typing import Generator

from src import check_time
from src.game.player import Player


class GameManager:
    # Includes rows, columns and both diagonals
    __win_lines = frozenset({
        frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9}),  # rows
        frozenset({1, 4, 7}), frozenset({2, 5, 8}), frozenset({3, 6, 9}),  # columns
        frozenset({1, 5, 9}), frozenset({3, 5, 7})  # diagonals
    })

    __player_1 = Player("Player 1")
    __player_2 = Player("Player 2")

    current_player: Player = None

    __buttons_pressed = 0

    @classmethod
    def get_players(cls) -> tuple[Player, Player]:
        return cls.__player_1, cls.__player_2

    @classmethod
    def set_player_1(cls, username: str):
        cls.__player_1 = Player(username)

    @classmethod
    def set_player_2(cls, username: str):
        cls.__player_2 = Player(username)

    @classmethod
    def increment_buttons_pressed(cls) -> None:
        cls.__buttons_pressed += 1

    @classmethod
    def set_marks(cls) -> None:
        if randrange(1, 201) & 1:
            cls.__player_1.mark = 'X'
            cls.__player_2.mark = 'O'

            cls.current_player = cls.__player_1
        else:
            cls.__player_1.mark = 'O'
            cls.__player_2.mark = 'X'

            cls.current_player = cls.__player_2

    @classmethod
    def reset_buttons_pressed(cls) -> None:
        cls.__buttons_pressed = 0

    @classmethod
    def reset_scores(cls):
        cls.__player_1.reset_score()
        cls.__player_2.reset_score()

    @classmethod
    def reset_marked_spaces(cls):
        cls.__player_1.reset_marked_spaces()
        cls.__player_2.reset_marked_spaces()

    @classmethod
    def switch_current_player(cls) -> None:
        cls.current_player = cls.__player_1 \
            if (cls.current_player is cls.__player_2)\
            else cls.__player_2

    @classmethod
    def __get_possible_win_lines(cls, value: int) -> Generator[frozenset[int], None, None]:
        for line in cls.__win_lines:
            if value in line:
                yield line.difference({value})

    @classmethod
    def win_check(cls, value: int) -> bool:
        for line in cls.__get_possible_win_lines(value):
            if line.issubset(GameManager.current_player.marked_spaces):
                return True
        return False

    @classmethod
    def tie_check(cls) -> bool:
        return cls.__buttons_pressed == 9
