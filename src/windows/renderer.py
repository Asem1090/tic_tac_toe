# Custom libs
# from src.windows.windows_manager import WindowsManager


class Renderer:
    __up_to_date = True
    action_required = {}
    action_for_windows = {}

    def __init__(self):
        while True:
            if self.up_to_date:
                continue

            if self.action_required["start_window"]:
                self.update_start_window()

    @property
    def up_to_date(self):
        return self.__up_to_date

    def update_start_window(self):
        possible_actions = self.action_for_windows["start_window"]

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
