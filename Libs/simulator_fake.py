import sys
import os
import random
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import math

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

import json
import data_converter
import betting_tools

odds = []

NAME = "test"
prob = 0.095

with open(PATH + '../Data/dataset.json') as file:
    a = json.loads(file.read())

    for r in a:
        if (len(r['runners']) == 10):
            for p in r["runners"]:
                if (p["standing"] == 1):
                    odds.append(p['odd'])

gains = 0

hist = []

a = 0
b = 0
for i, j in enumerate(odds):
    if (random.random() < prob):
        gains += betting_tools.get_gain(odds[i], True)
        a += 1
    else:
        gains += betting_tools.get_gain(odds[i], False)
    b += 1
    hist.append(gains)

plt.plot(hist)
plt.title("Accuracy : {}%".format(math.floor(a / b * 10000) / 100))
plt.savefig(PATH + "../Models/Simulations/simulation_" + NAME + ".png")
