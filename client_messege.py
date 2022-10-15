from socket import socket, AF_INET, SOCK_STREAM
from common.variables import *
import sys
from common.utils import *
from common.prepare_message_to_json import *
from common.json_form import *
from logs.decoration import func_checker
from logs import client_log_config

error_text = "Write '-help'"
help_text = """
        first argument: '-a' - adress: "localhost"
        second argument: '-p' - standart port [7777]
        """ 


class client_message():
    @func_checker
    def initialization(self, addr, port):
        print("""If you write '-stop',  server will be stop\n
            if '-stop_me', your connect will be destroyed""")
        self.CLIENT_LOGGER.info("(DONE) Initialization connection")
        while True:
            try:
                self.socket_file = socket(AF_INET, SOCK_STREAM)
                self.socket_file.connect((addr, port))
                self.CLIENT_LOGGER.debug(f"(DONE) Connection. address: {addr}, port: {port}")
            except:
                self.CLIENT_LOGGER.critical(f"(FAILED) Connection. address: {addr}, port: {port}")
            self.message = input("\nWrite message: ")
            if self.message == "-stop_me":
                self.socket_file.close()
                self.CLIENT_LOGGER.critical("Client writed '-stop_me")
                break
            
            # CLIENT_LOGGER.info("(START) prepear and send message...")
            self.dict_form_message = json_message_client(self.message) 
            self.prepare_message_json_send = self.prepearing.send(self.dict_form_message)
            self.transaction.send_messege(self.socket_file, self.prepare_message_json_send)
            self.CLIENT_LOGGER.info("(DONE) message is sent")

            # CLIENT_LOGGER.info("(START) geting message")
            self.message_file = self.transaction.get_messege(self.socket_file)
            self.prepare_message_json_get = self.prepearing.get(self.message_file)
            self.CLIENT_LOGGER.info(f"(DONE) Got message: {self.prepare_message_json_get}")

            self.message_get = self.prepare_message_json_get["message"]
            self.action_get = self.prepare_message_json_get["action"]
            print(f"\nMessage from server:\n{self.message_get},\naction: {self.action_get}")
            self.socket_file.close()
            self.CLIENT_LOGGER.info("(DONE) Socket is close")
            
    def __init__(self, addr, host_l):
        self.CLIENT_LOGGER = logging.getLogger("client_message")
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


