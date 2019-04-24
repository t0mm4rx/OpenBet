import sys
import os
import random
import numpy as np
import json
import matplotlib.pyplot as plt

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(PATH + '../')
from Libs import data_converter

features, targets, odds = data_converter.get_dataset()

sum = np.array([0, 0, 0, 0, 0, 0, 0, 0])

for t in targets:
    sum = np.add(sum, t)

plt.hist(sum)
plt.savefig(PATH + "../Temp/dist_winners.png")
