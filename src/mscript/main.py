# Custom libs
from src.mscript.main_class import MainClass
from src.log.logger import Logger
from src.windows.renderer import Renderer


def main():
    Logger.debug("Ahmed")
    Renderer.start()

    main_instance = MainClass()
    main_instance.run()


if __name__ == "__main__":
    main()
