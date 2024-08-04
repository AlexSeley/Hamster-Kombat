import requests
from data import headers, config
import time
from functions import buy_upgrade
import schedule

link = "https://api.hamsterkombatgame.io/clicker/claim-daily-combo"


def comboReady(): return requests.post(link, headers=headers).json()


def checkCombo():
    url = "https://api21.datavibe.top/api/GetCombo"
    combo = requests.post(url).json()
    combo = combo["combo"]
    print(combo)

    if comboReady()["error_code"] == 'DAILY_COMBO_NOT_READY':
        boughtCombos = comboReady()["error_message"].split("combo:", 1)[1]
        boughtCombos = boughtCombos.splitlines(",")
        print(boughtCombos)


        for item in boughtCombos:
            combo.remove(item) #Добавить проверку есть ли вообще купленные карточки

        for item in combo:
            buy = buy_upgrade(idUpgrade=[item], price=config["combo_priceMax"], return_seconds=True)
            if buy:
                print(f"cooldownSeconds for {item}: {buy}")
                time.sleep(buy)
                buy_upgrade(idUpgrade=[item], price=config["combo_priceMax"])
            else:
                continue

        claim_daily_combo = "https://api.hamsterkombatgame.io/clicker/claim-daily-combo"
        requests.post(claim_daily_combo, headers=headers)

schedule.every().day.at("14:00").do(checkCombo)

while True:
    schedule.run_pending()
    time.sleep(3600)