import requests

config = {}

with open('source/configuration.txt', "r") as file:
    for line in file:
        key, value = map(str.strip, line.split(':', 1))
        if key == "token":
            config[key] = value
        else:
            config[key] = int(value) if value.isdigit() else None

headers = {
    'Accept': '*    /*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': f'Bearer {config["token"]}',
    'Connection': 'keep-alive',
    'Origin': 'https://hamsterkombatgame.io',
    'Referer': 'https://hamsterkombatgame.io/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'android',
    'Content-Type': 'application/json'
    }

link = "https://api.hamsterkombatgame.io/clicker/sync"


def sync(): return requests.post(link, headers=headers).json()