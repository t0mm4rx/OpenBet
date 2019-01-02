import sys
sys.path.insert(0, 'Libs')

import data_fetcher
import inputs_generator
from matplotlib import pyplot as plt
from neural_network import NeuralNetwork
import os

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

nn = NeuralNetwork(21, [1000, 700, 500], 3, learning_rate=0.001)

X_TRAINING = []
Y_TRAINING = []


for race in data_fetcher.data_races:
    for runner in race['participants']:
        Y_TRAINING.append(inputs_generator.runner_to_output(runner))
        X_TRAINING.append(inputs_generator.runner_to_input(runner, race))

average = 0
count = 0
losses = []

for _ in range(1000):
    for i in range(len(X_TRAINING)):
        a = nn.train(X_TRAINING[i], Y_TRAINING[i])
        average += a
        count += 1
        if (i % 100 == 99):
            print("Loss", round(average / count * 100, 2), "%")
            losses.append(round(average / count * 100, 2))
            count = 0
            average = 0
        if (i % 10000 == 9999):
            plt.clf()
            plt.plot(losses)
            plt.ylim(bottom=0, top=100)
            plt.savefig(PATH + 'evolution.png')
