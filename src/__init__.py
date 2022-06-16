# Built-in libs
from time import perf_counter

# Custom libs
from typing import Callable, TypeVar

from src.log.logger import Logger

RETURN_TYPE = TypeVar("RETURN_TYPE")


def __call_func(func: Callable[..., RETURN_TYPE], *args, **kwargs) -> RETURN_TYPE:
    func_name = func.__name__

    Logger.debug(f"Calling {func_name}")
    beginning = perf_counter()
    returned_value = func(*args, **kwargs)
    end = perf_counter()
    Logger.info(f"Called {func_name} successfully")

    message = f"TIME CHECK for '{func_name}': {end - beginning}"
    Logger.debug(message)
    print(message)

    return returned_value


def check_time(func: Callable[..., RETURN_TYPE]) -> Callable[..., RETURN_TYPE]:
    def check(*args, **kwargs) -> RETURN_TYPE:

        returned_value = None

        try:
            returned_value = __call_func(func, *args, **kwargs)
        except TypeError:
            args = args[:-1]
            returned_value = __call_func(func, *args, **kwargs)

        except Exception as E:
            Logger.error(f"Error: {E}")

        return returned_value

    return check
