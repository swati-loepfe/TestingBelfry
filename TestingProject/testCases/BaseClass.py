import inspect
import logging
import inspect


class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(name)s - %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger
