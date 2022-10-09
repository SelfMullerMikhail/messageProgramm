from socket import socket, AF_INET, SOCK_STREAM
from common.variables import *
import sys
from common.utils import *
from common.prepare_message_to_json import *
from common.json_form import *

error_text = "Write '-help'"
help_text = """
        first argument: '-a' - adress: "localhost"
        second argument: '-p' - standart port [7777]
        """ 


class client_message():

    def initialization(self, addr, host_l):
        print("""If you write '-stop',  server will be stop\n
            if '-stop_me', your connect will be destroyed""")
        while True:
            self.socket_file = socket(AF_INET, SOCK_STREAM)
            self.socket_file.connect((addr, host_l))
            self.message = input("\nWrite message: ")
            # self.message = "Hello! I am client."
            if self.message == "-stop_me":
                self.socket_file.close()
                break
            
            self.dict_form_message = json_message_client(self.message) 
            self.prepare_message_json_send = self.prepearing.send(self.dict_form_message)
            self.transaction.send_messege(self.socket_file, self.prepare_message_json_send)

            self.message_file = self.transaction.get_messege(self.socket_file)
            self.prepare_message_json_get = self.prepearing.get(self.message_file)

            self.message_get = self.prepare_message_json_get["message"]
            self.action_get = self.prepare_message_json_get["action"]
            print(f"\nMessage from server:\n{self.message_get},\naction: {self.action_get}")
            self.socket_file.close()

    def __init__(self, addr, host_l):
        self.prepearing = Prepare_message_to_json()
        self.transaction = Trasaction_Functions()
        self.initialization(addr, host_l)


if __name__ == "__main__":

    try:
        addr = sys.argv[1]
        if addr == "-a":
            addr = DEFAULT_LOCAL_ADRESS
        elif addr == '-help': 
            raise ValueError(help_text)
        port_ = sys.argv[2]
        if port_ == "-p":
            port_ = DEFAULT_PORT
        
    except:
        raise ValueError(error_text)
    cleint_connection = client_message(addr, int(port_))


