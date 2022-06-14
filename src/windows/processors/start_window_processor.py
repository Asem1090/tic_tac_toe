# Custom libs
from src import check_time
from src.log.logger import Logger
from src.windows.processors.game_window_processor import GameWindowProcessor
from src.windows.processors.login_window_processor import LoginWindowProcessor
from src.windows.processors.processor import Processor


class StartWindowProcessor(Processor):

    def __init__(self):
        super().__init__(
            "start_window",
            pvp_btn=self.__pvp_btn_pressed, pve_btn=self.__pve_btn_pressed,
            local_network_btn=self.__local_network_btn_pressed,
            player_1_login_btn=self.__player_1_login_btn_pressed, player_2_login_btn=self.__player_2_login_btn_pressed
        )

    def __pvp_btn_pressed(self) -> None:
        Logger.debug("Accessing and closing start_window")
        windows_manager = self.manager
        windows_manager.get_window("start_window").close()

        windows_manager.set_window("game_window", GameWindowProcessor)

        game_window_processor = windows_manager.get_processor("game_window")

        Logger.info("Calling reset_game (from game_window processor)")
        game_window_processor.reset_game()

        Logger.info("Calling show for game_window")
        game_window_processor.game_window.show()

    def __pve_btn_pressed(self) -> None:
        Logger.info("pve_btn_pressed called successfully")

    def __local_network_btn_pressed(self) -> None:
        Logger.info("local_network_btn_pressed called successfully")

    def __player_login_btn_pressed(self, title):
        self.manager.set_window("login_window", LoginWindowProcessor)

        login_window = self.manager.get_window("login_window")
        login_window.setWindowTitle(title)

        Logger.info("Calling show for login_window")
        login_window.show()

    def __player_1_login_btn_pressed(self):
        self.__player_login_btn_pressed("Player 1 Login")

    def __player_2_login_btn_pressed(self):
        self.__player_login_btn_pressed("Player 2 Login")
