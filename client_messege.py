from concurrent.futures import thread
from ctypes import WinError
from socket import socket, AF_INET, SOCK_STREAM
import threading
from common.variables import *
import sys
from logs.logs_code.decoration import func_checker
from logs.logs_code import client_log_config
from threading import Thread

help_text = """If Using without arguments, 
function will start with DEFAULT_ARGUMENTS (ip = '', port = 8888)""" 


class client_message():
    @func_checker
    def server_wrtiter(self):
        while True:
            try:
                self.msg_input = input(" ")
                if self.msg_input == "Exit":
                    self.CLIENT_LOGGER.debug("Exit")
                    self.sock.close()
                    break
                self.sock.send(self.msg_input.encode(ENCODING))
                self.CLIENT_LOGGER.info(f"Message send: {self.msg_input}")
            except:
                self.CLIENT_LOGGER.critical("Error connection")
                self.sock.close() 
                raise ConnectionError("Server is closed")
    @func_checker
    def server_listener(self):
        while True:     
            try:
                self.server_msg_get = self.sock.recv(1024).decode(ENCODING)
            except:
                self.CLIENT_LOGGER.critical("Error connection")
                self.sock.close()
                raise ConnectionError("Server is closed")
            else:
                if self.server_msg_get:
                    print(self.server_msg_get)
                    self.CLIENT_LOGGER.info(f"Message got: {self.server_msg_get}")
    @func_checker
    def client_start(self):
        with socket(AF_INET, SOCK_STREAM) as self.sock:
            self.sock.connect(self.ADDRESS)
            self.CLIENT_LOGGER.debug(f"Create echo cleint {self.sock}")
            writer_thread = threading.Thread(target=self.server_wrtiter)
            writer_thread.start()
            self.server_listener()

    @func_checker
    def __init__(self, addr=DEFAULT_LOCAL_ADRESS, host_l=DEFAULT_PORT):
        self.ADDRESS = (addr, host_l)
        self.CLIENT_LOGGER = logging.getLogger("client_message")
        self.CLIENT_LOGGER.debug(f"Got address: {self.ADDRESS}")
        self.client_start()




if __name__ == "__main__":
    try:
        i = 1
        addr_ = str(sys.argv[1])
        if addr_ == "-help":
            i -= 1
            raise ValueError(help_text) 
        port_ = int(sys.argv[2])
    except:
        print("\CLIENT START WITH DEFAULT ARGUMENTS")
        a = client_message()
    else:
        if i == 1:
            a = client_message()
