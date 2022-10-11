from distutils.log import Log
import sys, os, logging, logging.handlers

sys.path.append(os.path.join('..', os.getcwd()))
from common.variables import LOGGING_LEVEL



class Main_Loger:
    def __init__(self, name):
        # Create loger's maker
        self.SERVER_FORMATER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

        # Prepear name of file for loging
        self.PATH = os.path.dirname(os.path.abspath(__file__))
        self.PATH = os.path.join(self.PATH, "server_message.log")

        # Create lines for the return logs
        self.STREAM_HANDLER = logging.StreamHandler(sys.stderr)
        self.STREAM_HANDLER.setFormatter(self.SERVER_FORMATER)
        self.STREAM_HANDLER.setLevel(logging.ERROR)
        self.LOG_FILE = logging.handlers.TimedRotatingFileHandler(self.PATH, encoding="utf-8", interval=1, when="D")
        self.LOG_FILE.setFormatter(self.SERVER_FORMATER)

        # Create register and setting it
        self.SERVER_LOGGER = logging.getLogger(name)
        self.SERVER_LOGGER.addHandler(self.STREAM_HANDLER)
        self.SERVER_LOGGER.addHandler(self.LOG_FILE)
        self.SERVER_LOGGER.setLevel(LOGGING_LEVEL)
    def info(self, text):
        self.SERVER_LOGGER.info(text)
    def debug(self, text):
        self.SERVER_LOGGER.debug(text)
    def critical(self, text):
        self.SERVER_LOGGER.critical(text)
    def error(self, text):
        self.SERVER_LOGGER.error(text)
        

# Testing
if __name__ == "__main__":
    test = Main_Loger("server_message")
    test.critical("Critical Error")
    # SERVER_LOGGER.error("Error")
    # SERVER_LOGGER.debug("Testing information")
    # SERVER_LOGGER.info("Inforaminoly message")


