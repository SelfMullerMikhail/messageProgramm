import sys, os
from socket import *
sys.path.append(os.path.join('..', os.getcwd()))
from common.variables import *
from logs import utils_log_config


UTILS_LOGGER = logging.getLogger("utils")


class Trasaction_Functions():
# function for send and encoding message
    def send_messege(self, client, message):
        if type(client) != socket:
            UTILS_LOGGER.critical("Client is not socket")
            raise TypeError("Type(client) is not 'socket'")
        if type(message) != str:
            UTILS_LOGGER.critical("Message is not 'str' format")
            raise TypeError("Message is not 'str")
        self.client = client
        self.client.send(message.encode(ENCODING))
        UTILS_LOGGER.info(f"(DONE) Message is encoded and sent:")

# function for get and decoding message
    def get_messege(self, client):
        if type(client) != socket:
            UTILS_LOGGER.critical("Client is not socket")
            raise TypeError("Type(client) is not 'socket'")
        UTILS_LOGGER.info("Waiting message from client...")
        self.message_file_decode = client.recv(MAX_PACKAGE_LENGTH).decode(ENCODING)
        if type(self.message_file_decode) != str:
            UTILS_LOGGER.critical("Message is not 'str' format")
            raise TypeError("Impossible to decode the message")
        UTILS_LOGGER.info(f"(DONE) Got and decoding message: {self.message_file_decode}")
        return self.message_file_decode

