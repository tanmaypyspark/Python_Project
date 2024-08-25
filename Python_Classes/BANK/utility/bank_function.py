import os
import json
import datetime
import random
os.system('cls')

def get_conf(config):
    if os.path.exists(config):
        with open(config,'r') as f:
            data = f.read()
        return json.loads(data)
    else:
        return {}

def writeConf(config, path):
    print('Config:', config)
    print('Path:',path)
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii= False, indent=4)
    except Exception as e:
        print(f'Error: While save the data error occured, {e}')

def getid():
    now = datetime.datetime.now()
    nm = random.randint(10,100)

    return f'{now.strftime("%m")}{now.strftime("%y")}{nm}'

# print(getid())
# firstName = 'TANMAY'
# print(firstName[0:2])