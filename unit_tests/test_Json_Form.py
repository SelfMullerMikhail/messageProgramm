import unittest, sys, os
sys.path.append(os.path.join('..', os.getcwd()))
from common.json_form import *

class Test_json_form(unittest.TestCase):
    def test_type_client(self):
        self.assertIsInstance(json_message_client("hello"), dict)
        self.assertIsInstance(json_message_client(1), dict)
        self.assertIsInstance(json_message_client(1.1), dict)
        self.assertIsInstance(json_message_client([1, 2]), dict)
        self.assertIsInstance(json_message_client({"one": 1, "second": 2.1}), dict)
        
    def test_type_server(self):
        self.assertIsInstance(json_message_server("hello"), dict)
        self.assertIsInstance(json_message_server(1), dict)
        self.assertIsInstance(json_message_server(1.1), dict)
        self.assertIsInstance(json_message_server([1, 2]), dict)
        self.assertIsInstance(json_message_server({"one": 1, "second": 2.1}), dict)

    def test_type_error_client(self):
        self.assertRaises(TypeError, json_message_client)

    def test_type_error_server(self):
        self.assertRaises(TypeError, json_message_server)






if __name__ == "__main__":
    unittest.main()