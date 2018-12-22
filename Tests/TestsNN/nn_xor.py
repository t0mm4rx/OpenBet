import sys
sys.path.insert(0, 'Libs')

from neural_network import NeuralNetwork

nn = NeuralNetwork(2, [3], 1, learning_rate=0.1)

x_training = [ [0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0] ]
y_training = [ [0.0], [1.0], [1.0], [0.0] ]

average = 0

for i in range(10000):
    average += nn.train(x_training[i % 4], y_training[i % 4])
    if (i % 4 == 3):
        print(average / 4)
        average = 0

print(nn.guess([0, 0]))
