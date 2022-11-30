import time
from functools import wraps
import logging

logging.basicConfig(filename='Logging.log', encoding="utf-16", level=logging.DEBUG)


def calculate_time(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        """Function calculate executed time"""
        start = time.time()
        result = func(*arg, **kwargs)
        end = time.time()
        logging.info(f"The executed time of {func.__name__} is {end-start}")
        return result
    return wrapper

