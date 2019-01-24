import sys
sys.path.insert(0, 'Libs')
import os
import data_fetcher
import inputs_generator
import tensorflow as tf
import numpy as np

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

X_TRAINING = []
Y_TRAINING = []


for race in data_fetcher.data_races:
    for runner in race['participants']:
        Y_TRAINING.append(inputs_generator.runner_to_output(runner))
        X_TRAINING.append(inputs_generator.runner_to_input(runner, race))

X_TRAINING = np.array(X_TRAINING)
Y_TRAINING = np.array(Y_TRAINING)

model = tf.keras.models.Sequential()
model.add( tf.keras.layers.Flatten() )
model.add(tf.keras.layers.Dense(21, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(3000, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(3000, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(2000, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(3, activation=tf.nn.sigmoid))

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.03), loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_TRAINING, Y_TRAINING, epochs=100, batch_size=2)

#print(X_TRAINING)
#print(Y_TRAINING)
