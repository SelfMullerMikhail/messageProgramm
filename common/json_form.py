def json_message_client(message):
    try:
        message = str(message)
    except:
        raise TypeError("Wrong type. Message can not be change gor 'str'")
    message_done = {"from": "pass", "to":"pass", "action":"pass", "message": message}
    return message_done

def json_message_server(message):
    try:
        message = str(message)
    except:
        raise TypeError("Wrong type. Message can not be change gor 'str'")
    message_done = {"action":"pass", "message": message}
    return message_done