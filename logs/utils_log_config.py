import sys
import os
import logging
import logging.handlers
sys.path.append(os.path.join('..', os.getcwd()))
from common.variables import LOGGING_LEVEL

# Create loger's maker
SERVER_FORMATER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# Prepear name of file for loging
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, "utils.log")

# Create lines for the return logs
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding="utf-8", interval=1, when="D")
LOG_FILE.setFormatter(SERVER_FORMATER)

# Create register and setting it
UTILS_LOGGER = logging.getLogger("utils")
UTILS_LOGGER.addHandler(STREAM_HANDLER)
UTILS_LOGGER.addHandler(LOG_FILE)
UTILS_LOGGER.setLevel(LOGGING_LEVEL)

# Testing
if __name__ == "__main__":
    UTILS_LOGGER.critical("Critical Error")
    UTILS_LOGGER.error("Error")
    UTILS_LOGGER.debug("Testing information")
    UTILS_LOGGER.info("Inforaminoly message")


