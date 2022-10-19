import sys
import os
import logging
import logging.handlers
sys.path.append(os.path.join('..', os.getcwd()))
from common.variables import LOGGING_LEVEL



# Create loger's maker
hey = "hey"
SERVER_FORMATER = logging.Formatter(f'%(asctime)s %(levelname)s %(filename)s %(message)s')

# Prepear name of file for loging
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, "server_message.log")

# Create lines for the return logs
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding="utf-8", interval=1, when="D")
LOG_FILE.setFormatter(SERVER_FORMATER)

# Create register and setting it
SERVER_LOGGER = logging.getLogger("server_message")
SERVER_LOGGER.addHandler(STREAM_HANDLER)
SERVER_LOGGER.addHandler(LOG_FILE)
SERVER_LOGGER.setLevel(LOGGING_LEVEL)

# Testing
if __name__ == "__main__":
    SERVER_LOGGER.critical("Critical Error")
    SERVER_LOGGER.error("Error")
    SERVER_LOGGER.debug("Testing information")
    SERVER_LOGGER.info("Inforaminoly message")


