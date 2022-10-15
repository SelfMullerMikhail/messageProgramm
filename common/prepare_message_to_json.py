from asyncore import read
import json
from subprocess import call
from logs.decoration import func_checker


class Prepare_message_to_json():
    @func_checker
    def send(self, message):
        if type(message) != dict:
            return TypeError("Message is not 'dict")
        try:
            self.message_json_send_done = json.dumps(message)
        except:
            raise TypeError("Inpossible encode message")
        return self.message_json_send_done
    @func_checker
    def get(self, message):
        try:
            self.message_json_get = json.loads(message)
        except:
            raise TypeError("Inpossible decode message")
        return self.message_json_get
