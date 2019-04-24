import sys
import os
import random
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

import json
import data_converter

features = []
targets = []

with open(PATH + '../Data/dataset.json') as file:
    a = json.loads(file.read())

    for r in a:
        if (len(r['runners']) == 10):

            #print(data_converter.runner_features(r["runners"][2]))
            #exit()

            features.append(np.array(data_converter.features(r)))
            targets.append(np.array(data_converter.targets(r)))

print(np.array(features).shape)
print(np.array(targets).shape)

print("Data loaded")
model = tf.keras.Sequential([
    tf.keras.layers.Dense(723, activation='relu'),
    tf.keras.layers.Dense(10000, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(np.array(features), np.array(targets), epochs=10, validation_split=0.2)

print("Weights saved")
model.save_weights(PATH + "../Models/model.h5")

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.savefig("training.png")
