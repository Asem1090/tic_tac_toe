# Custom libs
# from src.windows.windows_manager import WindowsManager
from time import sleep
from _thread import start_new_thread


class Renderer:
    __up_to_date = True
    action_required = {}
    action_for_windows = {}

    @property
    def up_to_date(self):
        return self.__up_to_date

    @staticmethod
    def update_start_window():
        possible_actions = Renderer.action_for_windows["start_window"]

        if possible_actions["pvp_btn_pressed"]:
            pass
            # signal this function WindowsManager.windows["start_window"]["processor"].pvp_btn_pressed()

        elif possible_actions["pve_btn_pressed"]:
            pass
            # signal this function WindowsManager.windows["start_window"]["processor"].pve_btn_pressed()

        elif possible_actions["local_network_btn_pressed"]:
            pass
            # signal this function WindowsManager.windows["start_window"]["processor"].local_network_btn_pressed()

        possible_actions["pvp_btn_pressed"] = False
        possible_actions["pve_btn_pressed"] = False
        possible_actions["local_network_btn_pressed"] = False

    @staticmethod
    def start():
        start_new_thread(Renderer.run, ())

    @classmethod
    def run(cls) -> None:
        while True:
            sleep(0.001)
            if cls.up_to_date:
                continue

            if cls.action_required["start_window"]:
                cls.update_start_window()
