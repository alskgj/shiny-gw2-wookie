__author__ = 'zen'
import time


def get_timestamp():
    # seconds - unix timestamp
    # a month is: ~2629740 seconds
    return int(time.time())
