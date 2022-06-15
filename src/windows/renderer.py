# Built-in libs
from threading import Thread
from time import sleep
from typing import TYPE_CHECKING

# Custom libs
from src import IS_DAEMON
from src.log.logger import Logger

if TYPE_CHECKING:
    from src.windows.windows_manager import WindowsManager


class Renderer:
    manager: "WindowsManager" = None

    __up_to_date = True

    __action_required = {"game_window": False}

    __actions_for_windows = {
        "game_window":
            {"start_stop_timer_pressed": False}
    }

    @classmethod
    def set_manager(cls, manager):
        cls.manager = manager

    @classmethod
    def set_up_to_date_to_false(cls) -> None:
        cls.__up_to_date = False

    @classmethod
    def set_button_action_to_true(cls, window_name: str, action_name: str) -> None:
        cls.__up_to_date = False
        cls.__action_required[window_name] = True
        print(window_name)
        print(action_name)
        cls.__actions_for_windows[window_name][action_name] = True

    @classmethod
    def __update_game_window(cls):
        cls.__action_required["game_window"] = False

        for action in cls.__actions_for_windows:

            if action == "start_stop_timer_button_pressed":
                cls.__actions_for_windows["game_window"]["start_stop_timer_button_pressed"] = False
                cls.manager.get_processor("game_window").start_stop_timer_pressed()

    @classmethod
    def start(cls) -> bool:
        Logger.debug("Starting the renderer in a new thread")
        Thread(daemon=IS_DAEMON, target=cls.__run, args=()).start()
        # start_in_new_thread(cls.__run, (cls,))

        cls.start = lambda: False
        return True

    @classmethod
    def __run(cls) -> None:
        Logger.info("Running the renderer")
        while True:
            sleep(1)

            if cls.__up_to_date:
                continue

            Logger.info("Checking which windows need to be update")

            cls.__up_to_date = True

            if cls.__action_required["game_window"]:
                Logger.info("Calling update_game_window in a new thread")
                Thread(daemon=IS_DAEMON, target=cls.__update_game_window, args=()).start()
