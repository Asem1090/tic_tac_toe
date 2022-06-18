"""
This file manages the background processes of the game only.
"""

# Built-in libs.
from random import randrange
from typing import Generator, Union

# Custom libs.
from src import Logger
from src.game.player import Player


class GameManager:
    """
    This class manages all game processing, like setting the players objects and checking if somebody has won.
    """

    # Includes rows, columns and both diagonals.
    __win_lines = frozenset({
        frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9}),  # rows.
        frozenset({1, 4, 7}), frozenset({2, 5, 8}), frozenset({3, 6, 9}),  # columns.
        frozenset({1, 5, 9}), frozenset({3, 5, 7})  # diagonals.
    })

    # Setting default players objects.
    __player_1 = Player("Player 1")
    __player_2 = Player("Player 2")

    __current_player: Player = None

    __buttons_pressed = 0  # If 9 and nobody has won then it is a tie.

    # Setting default timer period.
    __timer_period = 5

    @classmethod
    def get_timer_period(cls) -> Union[int, float]:
        """
        A getter for GameManager.__timer_period.
        :return: Integer or float, represents the time each player has before their turn is over.
        """

        return cls.__timer_period

    @classmethod
    def get_players(cls) -> tuple[Player, Player]:
        """
        A getter for GameManager.__player_1 and GameManager.__player_2.
        :return: A tuple of both Player objects.
        """

        return cls.__player_1, cls.__player_2

    @classmethod
    def get_player_1(cls) -> Player:
        """
        A getter for GameManager.__player_1.
        :return: Player object, represents player 1.
        """

        return cls.__player_1

    @classmethod
    def get_current_player(cls) -> Player:
        """
        A getter for GameManager.__current_player.
        :return: Player object, represents the player whose turn is up.
        """

        return cls.__current_player

    @classmethod
    def set_timer_period(cls, value: Union[int, float]) -> None:
        """
        A setter for GameManager.__timer_period.
        :param value: A positive number.
        :return: None
        """

        # Checking if value is not a positive number.
        if not isinstance(value, (int, float)) or value < 0:
            Logger.warning(f"Value must be a positive number, got {value!r}")
            return

        cls.__timer_period = value

    @classmethod
    def set_player_1(cls, username: str) -> None:
        """
        A setter for GameManager.__player_1.
        :param username: A string, represents the username for GameManager.__player_1.
        :return: None
        """

        cls.__player_1 = Player(username)

    @classmethod
    def set_player_2(cls, username: str) -> None:
        """
        A setter for GameManager.__player_2.
        :param username: A string, represents the username for GameManager.__player_2.
        :return: None
        """

        cls.__player_2 = Player(username)

    @classmethod
    def set_marks(cls) -> None:
        """
        A setter for Player.mark; sets mark attribute for both Player objects, and sets GameManager.__current_player.
        :return: None
        """

        # Setting the marks and current_player randomly.
        if randrange(1, 201) & 1:
            cls.__player_1.mark = 'X'
            cls.__player_2.mark = 'O'

            cls.__current_player = cls.__player_1
        else:
            cls.__player_1.mark = 'O'
            cls.__player_2.mark = 'X'

            cls.__current_player = cls.__player_2

    @classmethod
    def increment_buttons_pressed(cls) -> None:
        """
        Increments GameManager.__buttons_pressed by 1.
        :return: None
        """

        cls.__buttons_pressed += 1

    @classmethod
    def reset_buttons_pressed(cls) -> None:
        """
        Sets GameManager.__buttons_pressed to 0.
        :return: None
        """

        cls.__buttons_pressed = 0

    @classmethod
    def reset_scores(cls) -> None:
        """
        Sets _Player__score for both players to 0.
        :return: None
        """

        cls.__player_1.reset_score()
        cls.__player_2.reset_score()

    @classmethod
    def reset_marked_spaces(cls) -> None:
        """
        Sets _Player__marked_spaces for both players to an empty set.
        :return: None
        """

        cls.__player_1.reset_marked_spaces()
        cls.__player_2.reset_marked_spaces()

    @classmethod
    def switch_current_player(cls) -> None:
        """
        Changes GameManager.__current_player from a player to the other.
        :return: None
        """

        cls.__current_player = cls.__player_1 \
            if (cls.__current_player is cls.__player_2)\
            else cls.__player_2

    @classmethod
    def win_check(cls, value: int) -> bool:
        """
        Checks whether a player has won.
        :param value: An integer, represents the position of the x/o button pressed (1-9).
        :return: A boolean, represents whether the player has won or not.
        """

        # Iterating through the possible win lines.
        for line in cls.__get_possible_win_lines(value):
            # Checking if the player has marked all 3 spaces in the line.
            if line.issubset(GameManager.__current_player.marked_spaces):
                return True
        return False

    @classmethod
    def tie_check(cls) -> bool:
        """
        Checks if all buttons are pressed.
        :return: A boolean, represents whether the game is a tie or not.
        """

        return cls.__buttons_pressed == 9

    @classmethod
    def __get_possible_win_lines(cls, value: int) -> Generator[frozenset[int], None, None]:
        """
        Gets the possible win lines depending on the button pressed.
        :param value: An integer, represents the position of the x/o button pressed (1-9).
        :return: A Generator function that returns frozensets of integers.
        """

        for line in cls.__win_lines:  # Iterating through all lines.
            if value in line:  # Checking if the space marked, aka value, is in the line.
                yield line.difference({value})  # Yields the line without the value.
