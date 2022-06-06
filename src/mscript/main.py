# Built-in libs
from threading import enumerate as thread_enumerate

# Custom libs
from src.log.logger import Logger
from src.mscript.main_class import MainClass


def main() -> None:
    Logger.debug("Beginning of program")

    Logger.debug("Creating MainClass object")
    main_instance = MainClass()
    Logger.info("MainClass object created")

    Logger.debug("Calling run from MainClass object")
    main_instance.run()
    Logger.info("run called from MainClass object")

    Logger.info("End of actual program")

    Logger.debug("Looping inside the threads")
    for thread in thread_enumerate():
        if thread.name != "MainThread":
            Logger.debug(f"Waiting for {thread.name} to finish")
            thread.join()
            Logger.info(f"{thread.name} closed")


if __name__ == "__main__":
    main()
