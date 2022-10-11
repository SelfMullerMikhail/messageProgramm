from socket import *
from common.json_form import *
from common.utils import *
from common.prepare_message_to_json import *
import sys, logging
from common.variables import *
from logs import server_log_config

error_text = "Write '-help'"
help_text = """
        first argument: '-a' - open for all ip adresses
        second argument: '-p' - standart port [7777]
        """ 

# Initialization server's loging
SERVER_LOGGER = logging.getLogger("server_message")



class server():

# Шnitialization socket, bind, and start listen.
    def initialization_socket(self, addr_argv, port_argv):
        try:
            self.socket_file = socket(AF_INET, SOCK_STREAM)
            self.socket_file.bind((addr_argv, port_argv))
            self.socket_file.listen()
            SERVER_LOGGER.debug(f"(DONE) Initialization_socket. addres: {addr_argv}, port: {port_argv}")
        except:
            SERVER_LOGGER.critical("(FEILD) Initialization_socket")


# start listen of client
    def while_server(self):
        while True:
            self.client, self.addr = self.socket_file.accept()
            SERVER_LOGGER.info(f"(DONE) Connection is done. Address: {self.addr}")
            
            self.message_file_decode = self.transaction.get_messege(self.client)
            SERVER_LOGGER.info(f"(DONE) Got message from {self.addr}")
            
            self.prepare_message_json_get = self.prepearing.get(self.message_file_decode)
            SERVER_LOGGER.info("(DONE) Loading JSON's process")
            
            self.message_get = self.prepare_message_json_get["message"]
            self.msg = f"Message: {self.message_get}\nfrom \nip:{self.addr[0]}\nport: {self.addr[1]}"
            print(self.msg)
            SERVER_LOGGER.info(f"(DONE) Prepear message for print: {self.msg}") 

            SERVER_LOGGER.info(f"(START) Preperar and send message for addres: {self.addr}")
            self.dict_form_message = json_message_server(f"Your ip: {self.addr[0]} \nYour port:{self.addr[1]}")
            self.prepare_message_json_send = self.prepearing.send(self.dict_form_message)
            self.transaction.send_messege(self.client, self.prepare_message_json_send)
            SERVER_LOGGER.info("(DONE) Prepear and send message")

            self.client.close()
            SERVER_LOGGER.debug("Close connection")

            if self.message_get == "-stop":
                SERVER_LOGGER.critical("Client said '-stop")
                break

    def __init__(self, addr_argv, port_argv):
        if not 1023 < port_argv < 65536:
            SERVER_LOGGER.critical(f'Incorrectly port 'f'{port_argv}. Possible address from 1024 to 65535')
            sys.exit()
        SERVER_LOGGER.debug(f"Port: {port_argv} is open.\n Connection address: {addr_argv}")
        self.prepearing = Prepare_message_to_json()
        self.transaction = Trasaction_Functions()
        self.initialization_socket(addr_argv, port_argv)
        print("Server is started\n")
        self.while_server()


if __name__ == "__main__":

    try:
        addr_argv = sys.argv[1]
        if addr_argv == "-a":
            addr_ = DEFAULT_IP_ADDRESS
        elif addr_argv == '-help': 
            raise ValueError(help_text)
        port_argv = sys.argv[2]
        if port_argv == "-p":
            port_ = DEFAULT_PORT
        
    except:
        raise ValueError(error_text)
    a = server(addr_, port_)