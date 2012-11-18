import logging
from scrapy import log as scrapy_log

__author__ = 'jeffmay'

class CommonLogger(object):
    """
    A wrapper class for writing messages to both a Django logger and the Scrapy logger.

    @TODO: Figure out how to incorporate Django Dynamic Scraper logging.
    """
    def __init__(self, name):
        self._django_logger = logging.getLogger(name)

    def log(self, msg, level=logging.DEBUG, *args, **kwargs):
        if scrapy_log.started is False:
            scrapy_log.start()
        scrapy_log.msg(msg, level=level, **kwargs)
        self._django_logger.log(level, msg, *args, **kwargs)

    def debug(self, msg, level=logging.DEBUG, *args, **kwargs):
        self.log(msg, level, *args, **kwargs)

    def info(self, msg, level=logging.INFO, *args, **kwargs):
        self.log(msg, level, *args, **kwargs)

    def warning(self, msg, level=logging.WARNING, *args, **kwargs):
        self.log(msg, level, *args, **kwargs)

    def error(self, msg, level=logging.ERROR, *args, **kwargs):
        self.log(msg, level, *args, **kwargs)


def getLogger(name):
    """
    Retrieve a logger for a given unique name.
    @note This makes it easy to log to both Scrapy and Django
    @param name: A name to associate with a logger, usually __name__
    @return: A logger associated with the given name
    """
    return CommonLogger(name)
