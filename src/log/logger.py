"""
Here is where the logging is done.
"""

# Built-in libs
from inspect import stack  # To get caller info.
from logging import config, getLogger
from os.path import basename
from threading import Thread, Lock


class Logger:
    """
    This class uses threads to log with Lock on the variables.
    """

    config.fileConfig(
        fname="log_settings.config"
    )  # The file with the log message format.
    __logger = getLogger(__name__)

    lock = Lock()

    @staticmethod
    def __message_correction(message: str) -> str:
        """
        Gets the caller's info and put it with message in a neat way.
        :param message: A string, the message to be logged.
        :return: A string, which is 'message' with the caller info added to it.
        """

        caller_info = stack()[2]  # Getting the caller's info.

        return (
            "\n"
            f"\tFILE: {basename(caller_info.filename)}\n"
            f"\tFUNC: {caller_info.function}\n"
            f"\tLINE: {caller_info.lineno}\n"
            f"\tMESSAGE: {message}\n"
        )

    @classmethod
    def threadless_debug(cls, message: str) -> None:
        """
        Logs with 'DEBUG' level, using the main thread.
        :param message: A string, which is whatever the user wants to log.
        :return: None
        """

        with cls.lock:
            cls.__logger.debug(cls.__message_correction(message))

    @classmethod
    def debug(cls, message: str) -> None:
        """
        Logs with 'DEBUG' level, in a new thread.
        :param message: A string, which is whatever the user wants to log.
        :return: None
        """

        with cls.lock:
            Thread(
                daemon=True,
                target=cls.__logger.debug,
                args=(cls.__message_correction(message),),
            ).start()

    @classmethod
    def info(cls, message: str) -> None:
        """
        Logs with 'INFO' level, in a new thread with lock on the variables.
        :param message: A string, which is whatever the user wants to log.
        :return: None
        """

        with cls.lock:
            Thread(
                daemon=True,
                target=cls.__logger.info,
                args=(cls.__message_correction(message),),
            ).start()

    @classmethod
    def warning(cls, message: str) -> None:
        """
        Logs with 'WARNING' level, in a new thread with lock on the variables.
        :param message: A string, which is whatever the user wants to log.
        :return: None
        """

        with cls.lock:
            Thread(
                daemon=True,
                target=cls.__logger.warning,
                args=(cls.__message_correction(message),),
            ).start()

    @classmethod
    def error(cls, message: str) -> None:
        """
        Logs with 'ERROR' level, in a new thread with lock on the variables.
        :param message: A string, which is whatever the user wants to log.
        :return: None
        """

        with cls.lock:
            Thread(
                daemon=True,
                target=cls.__logger.error,
                args=(cls.__message_correction(message),),
            ).start()

    @classmethod
    def exception(cls, message: str) -> None:
        """
        Logs with 'EXCEPTION' level, in a new thread with lock on the variables.
        :param message: A string, which is whatever the user wants to log.
        :return: None
        """

        with cls.lock:
            Thread(
                daemon=True,
                target=cls.__logger.exception,
                args=(cls.__message_correction(message),),
            ).start()

    @classmethod
    def critical(cls, message: str) -> None:
        """
        Logs with 'CRITICAL' level, in a new thread with lock on the variables.
        :param message: A string, which is whatever the user wants to log.
        :return: None
        """

        with cls.lock:
            Thread(
                daemon=True,
                target=cls.__logger.critical,
                args=(cls.__message_correction(message),),
            ).start()
