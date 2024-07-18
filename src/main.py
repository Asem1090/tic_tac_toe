"""
This is where the main method is.
"""

# Built-in libs
from threading import (
    enumerate as thread_enumerate,
)  # Changing the name to avoid replacing enumerate built-in function.

# Custom libs
from log.logger import Logger
from mscript.main_class import MainClass


def main() -> None:
    """
    Here is where MainClass is used and where we confirm all threads close properly.
    :return: None
    """

    Logger.debug("Creating MainClass object")
    main_instance = MainClass()
    Logger.info("MainClass object created")

    main_instance.run()

    # Making sure all threads close before the main thread closes.
    for thread in thread_enumerate():
        if thread.name != "MainThread":
            Logger.threadless_debug(f"Waiting for {thread.name} to finish")
            thread.join()
            Logger.threadless_debug(f"{thread.name} closed")


if __name__ == "__main__":
    main()
