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

NAME = "model_newtraining"

"""
# Loading features and target for every race with 8+ runners
with open(PATH + '../Data/dataset.json') as file:
    a = json.loads(file.read())

    for r in a:
        if (len(r['runners']) >= 8):
            c = r
            c['runners'] = data_converter.filter_runners(8, r['runners'])

            if (len(np.array(data_converter.targets(c)).shape) > 0 and len(c['runners']) == 8):
                features.append(np.array(data_converter.features(c)))
                targets.append(np.array(data_converter.targets(c)))
"""
features, targets, _ = data_converter.get_dataset()

# Creating model and learning from data
print()
print(np.array(features).shape)
print(np.array(targets).shape)
print()


print("Data loaded")
model = tf.keras.Sequential([
    tf.keras.layers.Dense(653, activation='relu'),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(8, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(np.array(features), np.array(targets), epochs=10, validation_split=0.2)

model.save(PATH + "../Models/" + NAME + ".h5")
print("Model saved")

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.savefig(PATH + "../Models/Graphs/training_" + NAME + ".png")
