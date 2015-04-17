__author__ = 'zen'

from config.constants import *
import requests
from json import loads

res = loads(requests.get(BASE+"api/"+VERSION+FORMAT+"types").text)
print()