# Built-in libs
from inspect import stack
from logging import config, getLogger
from os.path import basename
from threading import Thread, Lock

# Custom libs
from src import IS_DAEMON


class Logger:

    config.fileConfig(fname="..\\..\\log_settings.config")
    __logger = getLogger(__name__)

    lock = Lock()

    @staticmethod
    def __message_correction(message: str) -> str:
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
        with cls.lock:
            cls.__logger.debug(cls.__message_correction(message))

    @classmethod
    def debug(cls, message: str) -> None:
        with cls.lock:
            Thread(daemon=IS_DAEMON, target=cls.__logger.debug, args=(cls.__message_correction(message),)).start()

    @classmethod
    def info(cls, message: str) -> None:
        with cls.lock:
            Thread(daemon=IS_DAEMON, target=cls.__logger.info, args=(cls.__message_correction(message),)).start()

    @classmethod
    def warning(cls, message: str) -> None:
        with cls.lock:
            Thread(daemon=IS_DAEMON, target=cls.__logger.warning, args=(cls.__message_correction(message),)).start()

    @classmethod
    def error(cls, message: str) -> None:
        with cls.lock:
            Thread(daemon=IS_DAEMON, target=cls.__logger.error, args=(cls.__message_correction(message),)).start()

    @classmethod
    def exception(cls, message: str) -> None:
        with cls.lock:
            Thread(daemon=IS_DAEMON, target=cls.__logger.exception, args=(cls.__message_correction(message),)).start()

    @classmethod
    def critical(cls, message: str) -> None:
        with cls.lock:
            Thread(daemon=IS_DAEMON, target=cls.__logger.critical, args=(cls.__message_correction(message),)).start()
