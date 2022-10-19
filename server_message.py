from socket import *
import sys, logging
from common.variables import *
from logs.logs_code.decoration import func_checker
from logs.logs_code import server_log_config
import select

help_text = """If Using without arguments, 
function will start with DEFAULT_ARGUMENTS (ip = '', port = 8888)""" 



class server():

    def read_requests(self, r_clients, all_clients):
        self.responses = {}
        for sock in r_clients:
                try:
                    self.data = sock.recv(1024).decode(ENCODING)
                    self.responses[sock] = self.data
                except:
                    self.text = f"Client (read) {sock.fileno()} {sock.getpeername()} disconnected"
                    self.SERVER_LOGGER.debug(self.text)
                    print(self.text)
                    all_clients.remove(sock)
        return self.responses


# ОЧЕНЬ ИНТЕРЕСНАЯ СИТУАЦИЯ.
# Не понимаю почему, но очень интересно. Именно здесь декоратор отрабатывает с 
# каждым сообщением на 1 раз больше. Это можно проверить в логах "func_checker.log" 
    @func_checker
    def write_requests(self, requests, w_clients, all_clients):
        for sock in w_clients:
            if sock in requests:
                resp = f"{sock.getpeername()}: {requests[sock]}".encode(ENCODING)

                for sock_send in all_clients:
                    try:
                        sock_send.send(resp)
                    except:
                        self.text = f"Client (write) {sock.fileno()} {sock.getpeername()} disconnected"
                        self.SERVER_LOGGER.debug(self.text)
                        print(self.text)
                        self.sock.close()
                        all_clients.remove(sock_send)

# Join 
    @func_checker
    def add_connection(self, address):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind(address)
        self.sock.listen(5)
        self.sock.settimeout(0.5)
        return self.sock


# Start listen of client
    @func_checker
    def while_server(self):
        
        while True:
            try:
                self.conn, self.addr = self.sock.accept()
            except:
                pass
            else:
                text = f"New connection {self.addr}"
                self.SERVER_LOGGER.debug(text)
                print(text)
                self.clients_all.append(self.conn)
            finally:
                self.r_clients = []
                self.w_clients = []

            try:
                self.r_clients, self.w_clients, self.e = select.select(self.clients_all, self.clients_all, self.clients_all, 5)
            except:
                pass
            self.requests = self.read_requests(self.r_clients, self.clients_all)
            if self.requests != {}:
                self.SERVER_LOGGER.info(f"Message: {self.requests}")
                self.write_requests(self.requests, self.w_clients, self.clients_all)

    def __init__(self, addr_argv=DEFAULT_IP_ADDRESS, port_argv=DEFAULT_PORT):
        self.SERVER_LOGGER = logging.getLogger("server_message")
        self.address = (addr_argv, port_argv)
        self.clients_all = []
        self.sock = self.add_connection(self.address)
        if not 1023 < port_argv < 65536:
            self.SERVER_LOGGER.critical(f'Incorrectly port 'f'{port_argv}. Possible address from 1024 to 65535')
            sys.exit()
        self.SERVER_LOGGER.debug(f"Port: {port_argv} is open.\n Connection address: {addr_argv}")
        print("Server is started\n")
        self.while_server()



if __name__ == "__main__":
    try:
        i = 1
        addr_ = str(sys.argv[1])
        if addr_ == "-help":
            i -= 1
            raise ValueError(help_text) 
        port_ = int(sys.argv[2])
    except:
        print("\nSERVER START WITH DEFAULT ARGUMENTS")
        a = server()
    else:
        if i == 1:
            a = server(addr_, port_)