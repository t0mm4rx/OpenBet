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

MODEL = "model_newtraining"

features, targets, odds = data_converter.get_dataset()

print("Data loaded,", len(features), "races")
model = tf.keras.models.load_model(PATH + "../Models/" + MODEL + ".h5")
print("Model loaded")

pred = model.predict_classes(np.array(features))
#print(pred)
print("Predictions made")

plt.hist(pred)
plt.savefig(PATH + "../Temp/dist_bets.png")

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

print("Average odd", math.floor(betting_tools.get_gain(np.average(odds), True) * 100) / 100)

plt.plot(hist)
plt.title("Accuracy : {}%".format(math.floor(a / b * 10000) / 100))
plt.savefig(PATH + "../Models/Simulations/simulation_" + MODEL + ".png")
