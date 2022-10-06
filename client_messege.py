from socket import socket, AF_INET, SOCK_STREAM
import sys

error_text = "Write '-help'"
help_text = """
        first argument: '-a' - adress: "localhost"
        second argument: '-p' - standart port [7777]
        """ 


class client_message():

    def send_message(self, info):
        self.info_encode = info.encode('utf-8')
        self.socket_file.send(self.info_encode)

    def get_message(self, socket_file):
        self.message_file = socket_file.recv(4096).decode('utf-8')
        return self.message_file

    def initialization(self, addr, host_l):
        self.socket_file = socket(AF_INET, SOCK_STREAM)
        self.socket_file.connect((addr, host_l))
        print("If you write 'stop',  server will be stop")
        self.message = input("Write message: ")
        self.send_message(self.message)
        self.message_file = self.get_message(self.socket_file)
        print(f"Message from server:\n {self.message_file}")
        self.socket_file.close()


    def __init__(self, addr, host_l):
        self.initialization(addr, host_l)


if __name__ == "__main__":

    try:
        addr = sys.argv[1]
        if addr == "-a":
            addr = "localhost"
        elif addr == '-help': 
            raise ValueError(help_text)
        port_ = sys.argv[2]
        if port_ == "-p":
            port_ = 7777
        # message = sys.argv[3]
        
    except:
        raise ValueError(error_text)
cleint_connection = client_message(addr, int(port_))


