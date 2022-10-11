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
PATH = os.path.join(PATH, "client_message.log")

# Create lines for the return logs
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding="utf-8", interval=1, when="D")
LOG_FILE.setFormatter(SERVER_FORMATER)

# Create register and setting it
CLIENT_LOGGER = logging.getLogger("client_message")
CLIENT_LOGGER.addHandler(STREAM_HANDLER)
CLIENT_LOGGER.addHandler(LOG_FILE)
CLIENT_LOGGER.setLevel(LOGGING_LEVEL)

# Testing
if __name__ == "__main__":
    CLIENT_LOGGER.critical("Critical Error")
    CLIENT_LOGGER.error("Error")
    CLIENT_LOGGER.debug("Testing information")
    CLIENT_LOGGER.info("Inforaminoly message")


