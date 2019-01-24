import numpy as np

class NeuralNetwork:

    def __init__(self, n_inputs, hiddens, n_outputs, learning_rate=0.01):
        self.hiddens = hiddens
        self.n_hiddens = len(hiddens)
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.learning_rate = learning_rate
        self.init()

    def init(self):
        self.weights = []
        self.biases = []
        self.weights.append(np.random.randn(self.hiddens[0], self.n_inputs))
        self.biases.append(np.random.randn(self.hiddens[0], 1))

        for i in range(1, self.n_hiddens):
            self.weights.append(np.random.randn(self.hiddens[i], self.hiddens[i - 1]))
            self.biases.append(np.random.randn(self.hiddens[i], 1))

        self.weights.append(np.random.randn(self.n_outputs, self.hiddens[-1]))
        self.biases.append(np.random.randn(self.n_outputs, 1))

    def forward(self, inputs):
        activations = []
        activations.append( self.activate( np.matmul(self.weights[0], np.transpose(np.array([inputs]))) + self.biases[0]))
        for i in range(1, self.n_hiddens + 1):
            activations.append( self.activate( np.matmul(self.weights[i], activations[i - 1]) + self.biases[i]))
        return activations

    def train(self, inputs, targets):
        pred = self.forward(inputs)
        errors = []
        gradients_weights = []
        gradients_bias = []
        # For output layer
        errors.append( pred[-1] - targets )
        gradients_weights.append( np.dot(errors[-1], np.transpose(pred[-2])))
        gradients_bias.append( np.sum(errors[-1], axis=1, keepdims=True) )

        # For each hidden layer
        for i in range(1, self.n_hiddens):
            layer = self.n_hiddens - i
            errors.append(np.multiply(np.dot(np.transpose(self.weights[layer + 1]), errors[-1]), 1 - np.power(pred[layer], 2)))
            gradients_weights.append( np.dot(errors[-1], np.transpose(pred[layer - 1]) ) )
            gradients_bias.append( np.sum(errors[-1], axis=1, keepdims=True) )

        # For inputs --> first hidden layer
        errors.append(np.multiply(np.dot(np.transpose(self.weights[1]), errors[-1]), 1 - np.power(pred[0], 2)))
        gradients_weights.append( np.dot(errors[-1], [inputs] ) )
        gradients_bias.append( np.sum(errors[-1], axis=1, keepdims=True) )

        for i in range(self.n_hiddens + 1):
            self.weights[i] -= self.learning_rate * gradients_weights[self.n_hiddens - i]
            self.biases[i] -= self.learning_rate * gradients_bias[self.n_hiddens - i]

    def cost(self, inputs, targets):
        sum = 0
        for i in range(len(inputs)):
            pred = self.forward(inputs[i])[-1][0][0]
            target = targets[i][0]
            sum += (target * np.log(pred) + (1 - target) * np.log(1 - pred))
        return (-1 / len(inputs)) * sum

    def activate(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, inputs):
        return self.forward(inputs)[-1]


"""
    Test
"""

"""
nn = NeuralNetwork(2, [1000], 1, learning_rate=0.07)
x_train = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
y_train = [
    [0],
    [1],
    [1],
    [0]
]

for i in range(100000):
    nn.train( x_train[i % 4], y_train[i % 4])
    print(nn.cost(x_train, y_train))

print(nn.predict(x_train[0]))
print(nn.predict(x_train[1]))
print(nn.predict(x_train[2]))
print(nn.predict(x_train[3]))
"""
