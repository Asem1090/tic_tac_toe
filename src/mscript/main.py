# Custom libs
from src.log.logger import Logger
from src.mscript.main_class import MainClass


def main():
    Logger.debug("Beginning of program")

    Logger.debug("Creating MainClass object")
    main_instance = MainClass()
    Logger.info("MainClass object created")

    Logger.debug("Calling run from MainClass object")
    main_instance.run()
    Logger.info("run called from MainClass object")

    Logger.info("End of program")


if __name__ == "__main__":
    main()
