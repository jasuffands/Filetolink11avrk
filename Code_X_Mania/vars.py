# (c) Code-x-Mania
import os
from os import getenv, environ
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')


class Var(object):
    API_ID = int(getenv('21773749'))
    API_HASH = str(getenv('42043fcad7b9a987691d0037ca74c1c1'))
    BOT_TOKEN = str(getenv('BOT_TOKEN'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'filetolinkprobot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('-1002117238737'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = set(int(x) for x in os.environ.get("6309983816", "").split())  
    #OWNER_ID=int(getenv('OWNER_ID'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('joy_yhhh'))
    A_G = str(getenv('A_G'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('mongodb+srv://orhehehudhdebhe:DUnSxfJQnZj4wbWs@cluster0.lehocm2.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('avrkhub', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
