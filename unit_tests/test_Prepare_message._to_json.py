import sys, os, unittest
from tests_text import *
sys.path.append(os.path.join('..', os.getcwd()))
from common.prepare_message_to_json import Prepare_message_to_json


class Test_prepare_message_to_json(unittest.TestCase):
    
    def test_type_transaction_send(self):
        self.example = Prepare_message_to_json()
        self.assertIsInstance(self.example.send(TEXT_DICT), str)

    def test_type_transaction_get(self):
        self.example = Prepare_message_to_json()
        self.assertIsInstance(self.example.get(TEXT_STR), dict)

    def test_correct_transaction_send(self):
        self.example = Prepare_message_to_json()
        self.assertEqual(self.example.send(TEXT_DICT), TEXT_STR)
    
    def test_type_error_send(self):
        self.example = Prepare_message_to_json()
        self.assertRaises(TypeError, self.example)

    def test_correct_transaction_get(self):
        self.example = Prepare_message_to_json()
        self.assertEqual(self.example.get(TEXT_STR), TEXT_DICT)

    def test_type_error_get(self):
        self.example = Prepare_message_to_json()
        self.assertRaises (TypeError, self.example.send)

    def test_isTrue_transaction_send(self):
        self.example = Prepare_message_to_json()
        self.assertTrue(self.example.send(TEXT_WORD))

    def sets_isTrue_transaction_get(self):
        self.example = Prepare_message_to_json()
        self.assertTrue(self.example.get(TEXT_STR))

if __name__ == "__main__":
    unittest.main()