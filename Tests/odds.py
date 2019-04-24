import sys
import os
import random

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(PATH + '../')

import json
from Libs import data_converter

musiques = []

with open(PATH + '../Data/dataset.json') as file:
    a = json.loads(file.read())

    for r in a:
        s = 0
        for p in r['runners']:
            s += p["odd"]
        print(s)
