from inspect import stack
from logging import config, getLogger
from os.path import basename
from threading import Thread


class Logger:

    config.fileConfig(fname="..\\..\\log_settings.config")
    __logger = getLogger(__name__)

    @staticmethod
    def message_correction(message: str) -> str:
        st = stack()[2]
        message = (
            "\n"
            f"\tFile Name: {basename(st.filename)}\n"
            f"\tFunc Name: {st.function}\n"
            f"\tLine No.: {st.lineno}\n"
            f"\tMessage: {message}\n"
        )
        return message

    @classmethod
    def debug(cls, message: str) -> None:
        Thread(target=cls.__logger.debug, args=(cls.message_correction(message),)).start()

    @classmethod
    def info(cls, message: str) -> None:
        Thread(target=cls.__logger.info, args=(cls.message_correction(message),)).start()

    @classmethod
    def warning(cls, message: str) -> None:
        Thread(target=cls.__logger.warning, args=(cls.message_correction(message),)).start()

    @classmethod
    def error(cls, message: str) -> None:
        Thread(target=cls.__logger.error, args=(cls.message_correction(message),)).start()

    @classmethod
    def exception(cls, message: str) -> None:
        Thread(target=cls.__logger.exception, args=(cls.message_correction(message),)).start()

    @classmethod
    def critical(cls, message: str) -> None:
        Thread(target=cls.__logger.critical, args=(cls.message_correction(message),)).start()
