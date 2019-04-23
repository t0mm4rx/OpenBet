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
        if (not race["distance"] in res):
            res.append(race["distance"])

with open(PATH + "Outputs/distances.json", "w+") as file:
    file.write(json.dumps(res))
