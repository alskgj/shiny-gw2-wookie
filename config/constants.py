__author__ = 'zen'

BASE = "https://www.gw2spidy.com/api/"
VERSION = "v0.9/"
FORMAT = "json/"

# Item id's, found with loads(requests.get(BASE+VERSION+FORMAT+"types").text)
ARMOR = "0"
WEAPON = "18"
CONSUMABLE = "3"
CRAFTING_MATERIAL = "5"
MINI = "11"
UPGRADE_COMPONENT = "17"
TROPHY = "16"
