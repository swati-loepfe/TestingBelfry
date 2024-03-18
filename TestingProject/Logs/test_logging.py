import logging


def test_logging():
    logger = logging.getLogger(__name__)

    filehandler=logging.FileHandler('logfile.log')
    logger.addHandler(filehandler)
    formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(name)s - %(message)s")
    filehandler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.debug("Debug:")
    logger.info("Info:")
    logger.warning("Warning:")
    logger.error("Error:")
    logger.critical("Critical:")




