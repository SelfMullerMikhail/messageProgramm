from ctypes import WinError
from socket import socket, AF_INET, SOCK_STREAM
from common.variables import *
import sys
from logs.logs_code.decoration import func_checker
from logs.logs_code import client_log_config
from threading import Thread

help_text = """If Using without arguments, 
function will start with DEFAULT_ARGUMENTS (ip = '', port = 8888)""" 


class client_message():
    def write_message(self, obj):
        # Не придумал я как нормально реализовать нормальный выход(
        if obj == self.counter:
            self.msg = input()
            if self.msg == "Exit":
                self.counter - 0 
            return self.msg
        if obj == self.counter:
            return "Exit"
        



    @func_checker
    def echo_client_writer(self):
        with socket(AF_INET, SOCK_STREAM) as self.sock:
            self.sock.connect(self.ADDRESS)
            self.CLIENT_LOGGER.debug(f"Create echo cleint {self.sock}")
            while True:     
                self.msg = self.write_message(1)
                if self.msg == "Exit":
                    self.CLIENT_LOGGER.critical("EXIT")
                    # break
                    sys.exit()
                try:
                    self.sock.send(self.msg.encode(ENCODING))
                except:
                    raise WinError("Server disconnect")

    @func_checker
    def echo_client_listener(self):
        with socket(AF_INET, SOCK_STREAM) as self.sock:
            self.sock.connect(self.ADDRESS)
            self.CLIENT_LOGGER.debug(f"Create listener socket: {self.sock}")
            while True:
                self.msg = self.write_message(0)
                if self.msg == "Exit:":
                    # break
                    sys.exit()
                try:
                    self.data = self.sock.recv(1024).decode(ENCODING)
                    if self.data:
                        print(f"\n{self.data}")
                except:
                    raise WinError("Server disconnect")

    @func_checker
    def __init__(self, addr=DEFAULT_LOCAL_ADRESS, host_l=DEFAULT_PORT):
        self.ADDRESS = (addr, host_l)
        self.CLIENT_LOGGER = logging.getLogger("client_message")
        self.counter = 1

        self.CLIENT_LOGGER.debug(f"Got info: {self.ADDRESS}") 
        self.echo_listener = Thread(target=self.echo_client_listener)
        self.echo = Thread(target=self.echo_client_writer)
        self.echo_listener.start()
        self.CLIENT_LOGGER.debug("Listener is started")
        self.CLIENT_LOGGER.debug("Writer is started")
        self.echo.start()




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
