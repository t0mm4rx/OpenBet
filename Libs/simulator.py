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

features = []
targets = []
odds = []

MODEL = "weak_model"

with open(PATH + '../Data/dataset.json') as file:
    a = json.loads(file.read())

    for r in a:
        if (len(r['runners']) == 10):
            features.append(np.array(data_converter.features(r)))
            targets.append(np.array(data_converter.targets(r)))
            for p in r["runners"]:
                if (p["standing"] == 1):
                    odds.append(p['odd'])


print("Data loaded")
model = tf.keras.models.load_model(PATH + "../Models/" + MODEL + ".h5")
print("Model loaded")

pred = model.predict_classes(np.array(features))
#print(pred)

gains = 0

hist = []

a = 0
b = 0
for i, j in enumerate(pred):
    if (targets[i][j] == 1):
        gains += betting_tools.get_gain(odds[i], True)
        a += 1
    else:
        gains += betting_tools.get_gain(odds[i], False)
    b += 1
    hist.append(gains)

plt.plot(hist)
plt.title("Accuracy : {}%".format(math.floor(a / b * 10000) / 100))
plt.savefig(PATH + "../Models/Simulations/simulation_" + MODEL + ".png")
