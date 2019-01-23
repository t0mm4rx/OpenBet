import tensorflow as tf
import numpy as np

x_train = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])

y_train = np.array([
    [0],
    [1],
    [1],
    [0],
])

model = tf.keras.models.Sequential()
model.add( tf.keras.layers.Flatten() )
model.add(tf.keras.layers.Dense(8, activation=tf.nn.tanh))
model.add(tf.keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1), loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=1000, batch_size=1)

print(model.predict_proba(x_train))
