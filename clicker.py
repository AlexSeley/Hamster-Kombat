import requests
from data import headers, sync
import time
import json

def syncTaps(): return sync()["clickerUser"]

def availableTaps(): return syncTaps()["availableTaps"]
def maxTaps(): return syncTaps()["maxTaps"]

def tapper():
    link = "https://api.hamsterkombatgame.io/clicker/tap"
    data = {
        "availableTaps": 0,
        "count": maxTaps(),
        "timestamp": int(time.time())}

    data = json.dumps(data)

    try:
        res = requests.post(link, headers=headers, data=data)
    except Exception as ex:
        print(ex)


while True:
    if availableTaps() == maxTaps():
        tapper()
        print("Tap")
    else:
        time.sleep(50)