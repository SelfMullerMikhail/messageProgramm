import sys, os, logging, logging.handlers
from functools import wraps

from logs.logs_code.get_way import get_way
sys.path.append(os.path.join('..', os.getcwd()))
from common.variables import ENCODING, LOGGING_LEVEL

def loggin_function(name_first_function, name_function,  args):
    # Create loger's maker
    SERVER_FORMATER = logging.Formatter(f"%(asctime)5s \naction: {name_function}. from: {name_first_function}. \nargs:{args}")
    
    way = get_way(__file__, 2)
    # Prepear name of file for loging
    # PATH = os.path.dirname(os.path.abspath(__file__))
    PATH = os.path.join(way, "func_checker.log")

    # Create lines for the return logs
    STREAM_HANDLER = logging.StreamHandler(sys.stderr)
    STREAM_HANDLER.setFormatter(SERVER_FORMATER)
    STREAM_HANDLER.setLevel(logging.ERROR)
    LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding=ENCODING, interval=1, when="D")
    LOG_FILE.setFormatter(SERVER_FORMATER)

    # Create register and setting it
    CLIENT_LOGGER = logging.getLogger("func_checker")
    CLIENT_LOGGER.addHandler(LOG_FILE)
    CLIENT_LOGGER.setLevel(LOGGING_LEVEL)
    CLIENT_LOGGER.info("")


def func_checker(func):    
    def decorate_finction(*args):
        main_function = func(*args) 
        name_function = func.__name__
        name_first_function = list(func.__globals__)[-1]
        loggin_function(name_first_function, name_function, args)
        return main_function
    return decorate_finction




# Testing
if __name__ == "__main__":
    text = func_checker
    # CLIENT_LOGGER.critical("Critical Error")
    # CLIENT_LOGGER.error("Error")
    # CLIENT_LOGGER.debug("Testing information")
    # CLIENT_LOGGER.info("Inforaminoly message")


