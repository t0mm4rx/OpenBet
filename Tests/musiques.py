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
        for p in r['runners']:
            musiques.append(p["musique"])

#print(len(musiques))

res = []

for musique in musiques:
    s = data_converter.musique(musique)
    res.append(s)

s = 0
for r in res:
    s += r

print("Mean:", s / len(res))
print("Max:", max(res))
print("Min:", min(res))
