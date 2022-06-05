# Custom libs
from src.log.logger import Logger
from src.windows.processors.processor import Processor


class StartWindowProcessor(Processor):

    def __init__(self, windows_manager):
        super().__init__(
            windows_manager, "start_window",
            pvp_btn=self.pvp_btn_pressed, pve_btn=self.pve_btn_pressed,
            local_network_btn=self.local_network_btn_pressed
        )

    def pvp_btn_pressed(self):
        Logger.debug("pvp_btn_pressed called")

    def pve_btn_pressed(self):
        Logger.debug("pve_btn_pressed called")

    def local_network_btn_pressed(self):
        Logger.debug("local_network_btn_pressed called")
