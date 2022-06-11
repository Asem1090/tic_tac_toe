from inspect import stack
from logging import config, getLogger
from os.path import basename
from threading import Thread


# Use lock
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
    def debug(cls, message: str) -> None:
        Thread(daemon=True, target=cls.__logger.debug, args=(cls.message_correction(message),)).start()

    @classmethod
    def info(cls, message: str) -> None:
        Thread(daemon=True, target=cls.__logger.info, args=(cls.message_correction(message),)).start()

    @classmethod
    def warning(cls, message: str) -> None:
        Thread(daemon=True, target=cls.__logger.warning, args=(cls.message_correction(message),)).start()

    @classmethod
    def error(cls, message: str) -> None:
        Thread(daemon=True, target=cls.__logger.error, args=(cls.message_correction(message),)).start()

    @classmethod
    def exception(cls, message: str) -> None:
        Thread(daemon=True, target=cls.__logger.exception, args=(cls.message_correction(message),)).start()

    @classmethod
    def critical(cls, message: str) -> None:
        Thread(daemon=True, target=cls.__logger.critical, args=(cls.message_correction(message),)).start()
