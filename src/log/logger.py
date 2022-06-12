# Built-in libs
from inspect import stack
from logging import config, getLogger
from os.path import basename
from threading import Thread


# Use lock
from typing import Callable


def start_in_new_thread(func: Callable, *args) -> None:
    Thread(daemon=True, target=func, args=args).start()


class Logger:

    config.fileConfig(fname="..\\..\\log_settings.config")
    __logger = getLogger(__name__)

    @staticmethod
    def message_correction(message: str) -> str:
        st = stack()[2]
        message = (
            "\n"
            f"\tFILE: {basename(st.filename)}\n"
            f"\tFUNC: {st.function}\n"
            f"\tLINE: {st.lineno}\n"
            f"\tMESSAGE: {message}\n"
        )
        return message

    @classmethod
    def threadless_debug(cls, message: str) -> None:
        cls.__logger.debug(cls.message_correction(message))

    @classmethod
    def debug(cls, message: str) -> None:
        start_in_new_thread(cls.__logger.debug, cls.message_correction(message))

    @classmethod
    def info(cls, message: str) -> None:
        start_in_new_thread(cls.__logger.info, cls.message_correction(message))

    @classmethod
    def warning(cls, message: str) -> None:
        start_in_new_thread(cls.__logger.warning, cls.message_correction(message))

    @classmethod
    def error(cls, message: str) -> None:
        start_in_new_thread(cls.__logger.error, cls.message_correction(message))

    @classmethod
    def exception(cls, message: str) -> None:
        start_in_new_thread(cls.__logger.exception, cls.message_correction(message))

    @classmethod
    def critical(cls, message: str) -> None:
        start_in_new_thread(cls.__logger.critical, cls.message_correction(message))
