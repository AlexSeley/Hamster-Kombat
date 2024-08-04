import requests
import json
import time
from data import headers, config

def buy_upgrade(idUpgrade: list, price=config["upgrade_priceMax"], return_seconds=False):
    res = 0
    link = 'https://api.hamsterkombatgame.io/clicker/buy-upgrade'

    priceId = _syncUpgrade(idUpgrade, ["price"])

    for i in priceId:
        priceItem = priceId[i]["price"]
        if priceItem <= price:
            continue
        else:
            print(f"Price {priceItem} is too high, should be lower than {price}")
            break

    for i in idUpgrade:
        data = {"timestamp": int(time.time()),
                "upgradeId": i}

        data = json.dumps(data)

        res = requests.post(link, headers=headers, data=data)

        if return_seconds:
            if res.status_code == 400:
                print("400")
                cooldownSeconds = (_syncUpgrade([i], ["cooldownSeconds"]))
                return cooldownSeconds[i]['cooldownSeconds']

        print(f"{i} - {res.status_code}")

def upgrades():    # Get information about all upgrades of the user
    link = "https://api.hamsterkombatgame.io/clicker/upgrades-for-buy"
    res = requests.post(link, headers=headers)
    upgradesForBuy = res.json()
    upgradesForBuy = upgradesForBuy["upgradesForBuy"]
    dic = [ele for ele in upgradesForBuy if isinstance(ele, dict)]

    return dic


def _syncUpgrade(upgradeId: list, elements: list):    # Get information about specific upgrades of the user
    dic = upgrades()
    return_dic = {}

    for item in dic:
        if item["id"] in upgradeId:
            item_dic = {'id': item["id"]}
            for element in elements:
                item_dic[element] = item[element]
                return_dic[item["id"]] = item_dic

    return return_dic