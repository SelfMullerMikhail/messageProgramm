from email.mime import message
from msilib.schema import Error
import sys
from socket import *

error_text = "Write '-help'"
help_text = """
        first argument: '-a' - open for all ip adresses
        second argument: '-p' - standart port [7777]
        """ 


class server():

# function for get and decoding message
    def get_messege(self, client):
        self.messege_file_decode = client.recv(1024).decode('utf-8')
        return self.messege_file_decode

# function for send and encoding message
    def send_messege(self, client, message):
        self.client = client
        self.client.send(message.encode("utf-8"))

# Шnitialization socket, bind, and start listen.
    def initialization_socket(self, addr_argv, port_argv):
        self.socket_file = socket(AF_INET, SOCK_STREAM)
        self.socket_file.bind((addr_argv, port_argv))
        self.socket_file.listen()

# start listen of client
    def while_server(self):
        while True:
            self.client, self.addr = self.socket_file.accept()
            self.message_file_decode = self.get_messege(self.client)
            self.msg = f"Message: {self.message_file_decode}\nfrom \n ip:{self.addr[0]}\n port: {self.addr[1]}"
            print(self.msg)
            self.send_messege(self.client, "Your" + self.msg)
            self.client.close()
            if self.message_file_decode == "stop":
                break

    def __init__(self, addr_argv, port_argv):
        self.initialization_socket(addr_argv, port_argv)
        print("Server is started")
        self.while_server()


if __name__ == "__main__":

    try:
        addr_argv = sys.argv[1]
        if addr_argv == "-a":
            addr_ = ""
        elif addr_argv == '-help': 
            raise ValueError(help_text)
        port_argv = sys.argv[2]
        if port_argv == "-p":
            port_ = 7777
        a = server(addr_, port_)
    except:
        raise ValueError(error_text)