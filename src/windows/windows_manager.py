# Custom libs
from src.windows.controllers.start_window_controller import StartWindowController
from src.windows.processors.start_window_processor import StartWindowProcessor
from src.windows.renderer import Renderer


class WindowsManager:
    windows = {}

    @classmethod
    def set_start_window(cls) -> None:
        WindowsManager.windows["start_window"] = {}
        WindowsManager.windows["start_window"]["controller"] = StartWindowController()
        WindowsManager.windows["start_window"]["processor"] = StartWindowProcessor(cls)

        Renderer.action_required["start_window"] = False

        Renderer.action_for_windows["start_window"] = {
            "pve_btn_pressed": False,
            "pvp_btn_pressed": False,
            "local_network_btn_pressed": False
        }