import os
import json
import sys
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

sys.path.append(PATH + '../../')
from Libs import data_converter
import matplotlib.pyplot as plt

x_f = []
y_f = []

x_l = []
y_l = []

with open(PATH + "../dataset.json") as file:
    a = json.loads(file.read())

    for race in a:
        for runner in race['runners']:
            if (runner['standing'] == 1):
                x_f.append(data_converter.musique(runner['musique']))
                y_f.append(runner['race_numbers'])
            else:
                x_l.append(data_converter.musique(runner['musique']))
                y_l.append(runner['race_numbers'])

plt.scatter(x_f[0:1000], y_f[0:1000], alpha=.2)
plt.scatter(x_l[0:1000], y_l[0:1000], alpha=.2)
plt.savefig(PATH + "Outputs/musique_races.png")
