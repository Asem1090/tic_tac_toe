# Custom libs
from src.log.logger import Logger
from src.windows.processors.game_window_processor import GameWindowProcessor
from src.windows.processors.login_window_processor import LoginWindowProcessor
from src.windows.processors.processor import Processor


class StartWindowProcessor(Processor):

    def __init__(self):
        super().__init__(
            "start_window",
            pvp_btn=self.pvp_btn_pressed, pve_btn=self.pve_btn_pressed,
            local_network_btn=self.local_network_btn_pressed,
            player_1_login_btn=self.player_1_login_btn_pressed, player_2_login_btn=self.player_2_login_btn_pressed
        )

    def pvp_btn_pressed(self) -> None:
        Logger.debug("Accessing and closing start_window")
        windows_manager = self._windows_manager
        windows_manager.get_window("start_window").close()

        windows_manager.set_window("game_window", GameWindowProcessor)

        game_window_processor = windows_manager.get_processor("game_window")
        Logger.info("Calling set_game (from game_window processor)")
        game_window_processor.reset_game()
        Logger.info("Calling show for game_window")
        game_window_processor.game_window.show()

    def pve_btn_pressed(self) -> None:
        Logger.info("pve_btn_pressed called successfully")

    def local_network_btn_pressed(self) -> None:
        Logger.info("local_network_btn_pressed called successfully")

    def player_login_btn_pressed(self, title):
        self._windows_manager.set_window("login_window", LoginWindowProcessor)

        login_window = self._windows_manager.get_window("login_window")
        login_window.setWindowTitle(title)

        Logger.info("Calling show for login_window")
        login_window.show()

    def player_1_login_btn_pressed(self):
        self.player_login_btn_pressed("Player 1 Login")

    def player_2_login_btn_pressed(self):
        self.player_login_btn_pressed("Player 2 Login")

