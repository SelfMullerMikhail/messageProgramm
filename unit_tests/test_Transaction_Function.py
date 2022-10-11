import sys, os, unittest
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from tests_text import *
sys.path.append(os.path.join('..', os.getcwd()))
from common.utils import Trasaction_Functions
from common.variables import *

class Test_Transaction_Funtion (unittest.TestCase):
    server_socket = None
    client_socket = None
    def setUp(self) -> None:
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.server_socket.listen(MAX_CONNECTIONS)

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((DEFAULT_LOCAL_ADRESS, DEFAULT_PORT))
        self.client, self.client_adress = self.server_socket.accept()

    def tearDown(self) -> None:
        self.client.close()
        self.client_socket.close()
        self.server_socket.close()


    def test_send_wrong_message(self):
        self.test_function = Trasaction_Functions()
        self.assertRaises(TypeError, self.test_function.send_messege, self.client_socket)

    def test_get_wrong_message(self):
        self.test_function = Trasaction_Functions()
        self.assertRaises(TypeError, self.test_function.get_messege, self.server_socket, TEXT_STR)

    def test_get_wrong_socket(self):
        self.test_function = Trasaction_Functions()
        self.assertRaises(TypeError, self.test_function.get_messege, self.server_socket, TEXT_STR)


    def test_get_message_type(self):
        self.test_function = Trasaction_Functions()
        self.test_function.send_messege(self.client_socket, TEXT_STR)
        self.assertIsInstance(self.test_function.get_messege(self.client), str)

    def test_get_message(self):
        self.test_function = Trasaction_Functions()
        self.test_function.send_messege(self.client_socket, TEXT_WORD)
        self.assertEqual(self.test_function.get_messege(self.client), TEXT_WORD)

    


if __name__ == "__main__":
    unittest.main()