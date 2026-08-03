from functools import wraps
from time import perf_counter

from dispatch.utils.logger import logger

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        logger.info("Starting %s", func.__name__)

        result = func(*args, **kwargs)

        elapsed = perf_counter() - start

        logger.info(
            "Finished %s in %.4f seconds",
            func.__name__,
            elapsed,
        )

        return result

    return wrapper