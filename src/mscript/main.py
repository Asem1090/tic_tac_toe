# Custom libs
from src.log.logger import Logger
from src.mscript.main_class import MainClass


def main():
    Logger.debug("Program's beginning")

    Logger.debug("Creating MainClass object")
    main_instance = MainClass()

    Logger.debug("Calling run from MainClass object")
    main_instance.run()

    Logger.info("Program's end")


if __name__ == "__main__":
    main()
