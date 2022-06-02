# Built-in libs
from time import sleep
from _thread import start_new_thread

# Custom libs
from src.log.logger import Logger


class Renderer:
    __up_to_date = True

    action_required = {
        "start_window": False
    }

    action_for_windows = {
        "start_window": {
            "pve_btn_pressed": False,
            "pvp_btn_pressed": False,
            "local_network_btn_pressed": False
        }
    }

    @classmethod
    @property
    def up_to_date(cls):
        return Renderer.__up_to_date

    # @classmethod
    # @up_to_date.setter
    # def up_to_date(self, value):
    #     Renderer.__up_to_date = bool(value)

    @staticmethod
    def update_start_window():
        possible_actions = Renderer.action_for_windows["start_window"]

        Logger.debug("Checking which button got pressed")
        if possible_actions["pvp_btn_pressed"]:
            Logger.debug("Signalling to execute pvp_btn_pressed from start window processor")
            # signal this function WindowsManager.windows["start_window"]["processor"].pvp_btn_pressed()

        elif possible_actions["pve_btn_pressed"]:
            Logger.debug("Signalling to execute pve_btn_pressed from start window processor")
            # signal this function WindowsManager.windows["start_window"]["processor"].pve_btn_pressed()

        elif possible_actions["local_network_btn_pressed"]:
            Logger.debug("Signalling to execute local_network_btn_pressed from start window processor")
            # signal this function WindowsManager.windows["start_window"]["processor"].local_network_btn_pressed()

        Logger.debug("Resetting the values of possible actions for start window to False")
        for action in possible_actions:
            possible_actions[action] = False

    @staticmethod
    def start():
        Logger.debug("Starting the renderer in a new thread")
        start_new_thread(Renderer.run, ())

    @staticmethod
    def run() -> None:
        Logger.info("Running the renderer")
        while True:
            sleep(0.001)
            if Renderer.__up_to_date:
                continue

            if Renderer.action_required["start_window"]:
                Logger.debug("Calling update_start_window")
                Renderer.update_start_window()
