# Built-in libs
from typing import TYPE_CHECKING

# Custom libs
from src.log.logger import Logger
from src.windows.processors.game_window_processor import GameWindowProcessor
from src.windows.processors.login_window_processor import LoginWindowProcessor
from src.windows.processors.processor import Processor

if TYPE_CHECKING:
    from src.windows.windows_manager import WindowsManager


class StartWindowProcessor(Processor):

    def __init__(self, windows_manager: "WindowsManager"):
        super().__init__(
            windows_manager, "start_window",
            pvp_btn=self.pvp_btn_pressed, pve_btn=self.pve_btn_pressed,
            local_network_btn=self.local_network_btn_pressed,
            player_1_login_btn=self.player_1_login_btn_pressed, player_2_login_btn=self.player_2_login_btn_pressed
        )

    def pvp_btn_pressed(self) -> None:
        Logger.debug("Getting start_window")
        start_window = self._windows_manager.get_window("start_window")
        Logger.info("Got start_window")

        Logger.debug("Closing start_window")
        start_window.close()
        Logger.info("Closed start_window successfully")

        Logger.debug("Creating game_window")
        self._windows_manager.set_window("game_window", GameWindowProcessor)
        Logger.info("Created game_window successfully")

        Logger.debug("Calling show for game_window")
        self._windows_manager.get_processor("game_window").show_game_window()
        Logger.info("Called show for game_window successfully")

        Logger.info("pvp_btn_pressed called successfully")

    def pve_btn_pressed(self) -> None:
        Logger.info("pve_btn_pressed called successfully")

    def local_network_btn_pressed(self) -> None:
        Logger.info("local_network_btn_pressed called successfully")

    def player_login_btn_pressed(self, title):
        Logger.debug("Creating login_window")
        self._windows_manager.set_window("login_window", LoginWindowProcessor)
        Logger.info("Created login_window successfully")

        login_window = self._windows_manager.get_window("login_window")
        login_window.setWindowTitle(title)

        Logger.debug("Calling show for login_window")
        login_window.show()
        Logger.info("Called show for login_window successfully")

    def player_1_login_btn_pressed(self):
        self.player_login_btn_pressed("Player 1 Login")

    def player_2_login_btn_pressed(self):
        self.player_login_btn_pressed("Player 2 Login")

