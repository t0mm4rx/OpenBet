import os
import json
import sys
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

sys.path.append(PATH + '../../')
from Libs import data_converter
import matplotlib.pyplot as plt

res = []

with open(PATH + "../dataset.json") as file:
    a = json.loads(file.read())

    for race in a:
        for runner in race['runners']:
            if (not runner['race'] in res):
                res.append(runner['race'])

with open(PATH + "Outputs/races.json", "w+") as file:
    file.write(json.dumps(res))
