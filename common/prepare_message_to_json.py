from asyncore import read
import json



class Prepare_message_to_json():
    def send(self, message):
        if type(message) != dict:
            return TypeError("Message is not 'dict")
        try:
            self.message_json_send_done = json.dumps(message)
        except:
            raise TypeError("Inpossible encode message")
        return self.message_json_send_done

    def get(self, message):
        try:
            self.message_json_get = json.loads(message)
        except:
            raise TypeError("Inpossible decode message")
        return self.message_json_get
