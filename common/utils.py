import sys, os
from socket import *
sys.path.append(os.path.join('..', os.getcwd()))
from common.variables import *



class Trasaction_Functions():
# function for send and encoding message
    def send_messege(self, client, message):
        if type(client) != socket:
            raise TypeError("Type(client) is not 'socket'")
        if type(message) != str:
            raise TypeError("Message is not 'str")
        self.client = client
        self.client.send(message.encode(ENCODING))

# function for get and decoding message
    def get_messege(self, client):
        if type(client) != socket:
            raise TypeError("Type(client) is not 'socket'")
        self.message_file_decode = client.recv(MAX_PACKAGE_LENGTH).decode(ENCODING)
        if type(self.message_file_decode) != str:
            raise TypeError("Impossible to decode the message")
        return self.message_file_decode

