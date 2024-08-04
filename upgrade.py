import time
from data import config
from functions import buy_upgrade, upgrades, _syncUpgrade


def best_upgrade():
    dic = upgrades()
    profitItems = []

    upgradeIds = [item["id"] for item in dic]
    elements = ["price", "profitPerHourDelta", "isAvailable", "isExpired"]
    syncedUpgrades = _syncUpgrade(upgradeIds, elements)

    for upgrade in syncedUpgrades:
        item = syncedUpgrades[upgrade]
        if item["isAvailable"] and not item["isExpired"] and item["price"]:
            if (item["profitPerHourDelta"] / item["price"]) >= 0.00085:    # The higher, the more profit
                profitItems.append(item["id"])

    print(profitItems)
    buy_upgrade(profitItems, price=config['combo_priceMax'])


while True:
    best_upgrade()
    time.sleep(100)