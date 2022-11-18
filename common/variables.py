import logging

"""Константы"""


# Порт поумолчанию для сетевого ваимодействия
DEFAULT_PORT = 8888
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = ""
#IP адрес по умолчанию для клиента
DEFAULT_LOCAL_ADRESS = "localhost"
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'

# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'

#Loging level now
LOGGING_LEVEL = logging.DEBUG
