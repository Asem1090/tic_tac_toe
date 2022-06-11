# Built-in libs
from threading import enumerate as thread_enumerate
from tracemalloc import start, take_snapshot

# Custom libs
from src.log.logger import Logger
from src.mscript.main_class import MainClass


def main() -> None:
    # start()
    Logger.debug("Creating MainClass object")
    main_instance = MainClass()
    Logger.info("MainClass object created")

    # [print(item) for item in take_snapshot().statistics("filename")]

    main_instance.run()

    for thread in thread_enumerate():
        if thread.name != "MainThread":
            Logger.threadless_debug(f"Waiting for {thread.name} to finish")
            thread.join()
            Logger.threadless_debug(f"{thread.name} closed")


if __name__ == "__main__":
    main()
