import sys
import os
import random
import numpy as np

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(PATH + '../')

import json
from Libs import data_converter

musiques_f = []
courses_f = []
musiques_l = []
courses_l = []

with open(PATH + '../Data/dataset.json') as file:
    a = json.loads(file.read())

    for r in a:
        for p in r['runners']:
            if (p["standing"] == 1):
                musiques_f.append(data_converter.musique(p["musique"]))
                courses_f.append(p["race_numbers"])
            else:
                musiques_l.append(data_converter.musique(p["musique"]))
                courses_l.append(p["race_numbers"])

print("Winners")
print("Mean musique", np.average(musiques_f))
print("Mean races", np.average(courses_f))
print("Losers")
print("Mean musique", np.average(musiques_l))
print("Mean races", np.average(courses_l))
