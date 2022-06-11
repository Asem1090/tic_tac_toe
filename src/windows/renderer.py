# Built-in libs
from time import sleep
from threading import Thread

# Custom libs
from src.log.logger import Logger


class Renderer:
    __up_to_date = True

    __action_required = {}

    __actions_for_windows = {}

    @classmethod
    def set_up_to_date_to_true(cls) -> None:
        cls.__up_to_date = True

    @classmethod
    def set_button_action_to_true(cls, window_name: str, action_name: str) -> None:
        Logger.debug(f"Changing {window_name} in action_required to True")
        cls.__action_required[window_name] = True
        Logger.info(f"Changed {window_name} in action_required to True successfully")

        Logger.debug(f"Changing {action_name} in actions_for_windows to True")
        cls.__actions_for_windows[window_name][action_name] = True
        Logger.info(f"Changed {action_name} in actions_for_windows to True successfully")

    @classmethod
    def start(cls) -> bool:
        Logger.debug("Starting the renderer in a new thread")
        Thread(daemon=True, target=cls.run, args=())

        cls.start = lambda: False
        return True

    @classmethod
    def run(cls) -> None:
        Logger.info("Running the renderer")
        while True:
            sleep(0.001)

            if cls.__up_to_date:
                continue

            cls.__up_to_date = True

            # if Renderer.action_required["start_window"]:
            #     Logger.debug("Calling update_start_window in a new thread")
            #     start_new_thread(Renderer.update_start_window, ())
