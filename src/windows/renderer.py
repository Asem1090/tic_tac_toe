# Built-in libs
from time import sleep
from _thread import start_new_thread

# Custom libs
from src.log.logger import Logger


class Renderer:
    __up_to_date = True

    __action_required = {}

    __actions_for_windows = {}

    @staticmethod
    def set_up_to_date_to_true() -> None:
        Renderer.__up_to_date = True

    @staticmethod
    def set_button_action_to_true(window_name: str, action_name: str) -> None:
        Logger.debug(f"Changing {window_name} in action_required to True")
        Renderer.__action_required[window_name] = True
        Logger.info(f"Changed {window_name} in action_required to True successfully")

        Logger.debug(f"Changing {action_name} in actions_for_windows to True")
        Renderer.__actions_for_windows[window_name][action_name] = True
        Logger.info(f"Changed {action_name} in actions_for_windows to True successfully")

    # @staticmethod
    # def update_start_window():
    #     possible_actions = Renderer.actions_for_windows["start_window"]
    #
    #     Logger.debug("Checking which button got pressed")
    #     if possible_actions["pvp_btn_pressed"]:
    #         Logger.debug("Signalling to execute pvp_btn_pressed from start window processor")
    #         # signal this function WindowsManager.windows["start_window"]["processor"].pvp_btn_pressed()
    #
    #     elif possible_actions["pve_btn_pressed"]:
    #         Logger.debug("Signalling to execute pve_btn_pressed from start window processor")
    #         # signal this function WindowsManager.windows["start_window"]["processor"].pve_btn_pressed()
    #
    #     elif possible_actions["local_network_btn_pressed"]:
    #         Logger.debug("Signalling to execute local_network_btn_pressed from start window processor")
    #         # signal this function WindowsManager.windows["start_window"]["processor"].local_network_btn_pressed()
    #
    #     Logger.debug("Resetting the values of possible actions for start window to False")
    #     for action in possible_actions:
    #         possible_actions[action] = False

    @staticmethod
    def start() -> bool:
        Logger.debug("Starting the renderer in a new thread")
        start_new_thread(Renderer.run, ())

        Logger.debug("Changing start to lambda: False")
        Renderer.start = lambda: False
        Logger.info("Changed start to lambda: False successfully")

        return True

    @staticmethod
    def run() -> None:
        Logger.info("Running the renderer")
        while True:
            sleep(0.001)

            if Renderer.__up_to_date:
                continue

            Logger.debug("Resetting Renderer.__up_to_date to True")
            Renderer.__up_to_date = True
            Logger.info("Reset Renderer.__up_to_date to True")

            # if Renderer.action_required["start_window"]:
            #     Logger.debug("Calling update_start_window in a new thread")
            #     start_new_thread(Renderer.update_start_window, ())

