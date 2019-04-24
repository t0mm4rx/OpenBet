import sys
import os
import random
import numpy as np

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(PATH + '../')

import json
from Libs import data_converter

s = 0
n = 0

with open(PATH + '../Data/dataset.json') as file:
    a = json.loads(file.read())

    for r in a:
        for p in r['runners']:
            s += p["odd"]
            n += 1

print(s / n)
