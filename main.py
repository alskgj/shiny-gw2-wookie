"""
__author__ = 'zen'

Idea: Parse all gathering materials from gw2spidy and save results.
Alert on big price changes.

DOCs:
gw2spidy API: https://github.com/rubensayshi/gw2spidy/wiki/API-v0.9
SQLAlchemy: http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html
"""

import requests
from json import loads

from config.constants import *
from DB.sqlalchemy_insert import  insert




query = loads(requests.get(BASE+VERSION+FORMAT+"all-items/"+CRAFTING_MATERIAL).text)

print("Fetched data of [{itemcount}] items...".format(itemcount=query["count"]))

#print(query)

# item is a dict, describing one item. interesting keys::
# 'name'
# 'data_id'
# 'type_id'
# 'sub_type_id'
# 'offer_availability'
# 'sale_availability'
# 'min_sale_unit_price'
# 'max_offer_unit_price'

# for item in query["results"]:
#     ~ do stuff

print("Crunching numbers...")
for item in query["results"]:
    name = item["name"]
    price = item["min_sale_unit_price"]

    offers = item["offer_availability"]
    # only interesting items...

