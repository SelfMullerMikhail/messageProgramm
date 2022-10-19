import sys, os
from socket import *
sys.path.append(os.path.join('..', os.getcwd()))
from common.variables import *
from logs.decoration import func_checker
from logs import utils_log_config




class Trasaction_Functions():
# function for send and encoding message
    def __init__(self):
        self.UTILS_LOGGER = logging.getLogger("utils")
    @func_checker
    def send_messege(self, client, message):
        if type(client) != socket:
            self.UTILS_LOGGER.critical("Client is not socket")
            raise TypeError("Type(client) is not 'socket'")
        if type(message) != str:
            self.UTILS_LOGGER.critical("Message is not 'str' format")
            raise TypeError("Message is not 'str")
        self.client = client
        self.client.send(message.encode(ENCODING))
        self.UTILS_LOGGER.info(f"(DONE) Message is encoded and sent:")

# function for get and decoding message
    @func_checker
    def get_messege(self, client):
        if type(client) != socket:
            self.UTILS_LOGGER.critical("Client is not socket")
            raise TypeError("Type(client) is not 'socket'")
        self.UTILS_LOGGER.info("Waiting message from client...")
        self.message_file_decode = client.recv(MAX_PACKAGE_LENGTH).decode(ENCODING)
        if type(self.message_file_decode) != str:
            self.UTILS_LOGGER.critical("Message is not 'str' format")
            raise TypeError("Impossible to decode the message")
        self.UTILS_LOGGER.info(f"(DONE) Got and decoding message: {self.message_file_decode}")
        return self.message_file_decode

