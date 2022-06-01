from logging import config, getLogger
from inspect import stack
from _thread import start_new_thread
from os.path import basename


class Logger:

    config.fileConfig(fname="..\\..\\log_settings.config")
    __logger = getLogger(__name__)

    @staticmethod
    def message_correction(message):
        st = stack()[2]
        message = (
            "\n"
            f"\tFile Name: {basename(st.filename)}\n"
            f"\tFunc Name: {st.function}\n"
            f"\tLine No.: {st.lineno}\n"
            f"\tMessage: {message}\n"
        )
        return message

    @staticmethod
    def debug(message):
        start_new_thread(Logger.__logger.debug, (Logger.message_correction(message),))

    @staticmethod
    def info(message):
        start_new_thread(Logger.__logger.debug, (Logger.message_correction(message),))

    @staticmethod
    def warning(message):
        start_new_thread(Logger.__logger.warning, (Logger.message_correction(message),))

    @staticmethod
    def exception(message):
        start_new_thread(Logger.__logger.exception, (Logger.message_correction(message),))

    @staticmethod
    def critical(message):
        start_new_thread(Logger.__logger.critical, (Logger.message_correction(message),))
