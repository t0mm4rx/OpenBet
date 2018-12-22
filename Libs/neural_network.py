"""
    NeuralNetwork class.
        - n_inputs (int): number of inputs
        - n_hidden (int[]): array with neurons number of each hidden layers given. Ex : [5, 4, 3] will create 3 hidden layers with 5, 4 and 3 neurons
        - n_output (int): number of outputs
        - load_weights(filename (str)): loads weights from file in the current model
        - save_weights(filename (str)): exports current weights in given file
        - train(input (int[]), output(int[])): train the network with given data
        - guess(input (int[])): realise a prediction of the given input
"""

import tensorflow as tf

class NeuralNetwork:

    def __init__(self, n_inputs, n_hiddens, n_outputs, learning_rate = 0.01):
        self.n_inputs = n_inputs
        self.n_hiddens = n_hiddens
        self.n_outputs = n_outputs
        self.learning_rate = learning_rate
        self.session = None
        self.optimizer = None
        self.forward = None
        self.init_tf()

    # Initializing tensorflow variables, weights and biases
    def init_tf(self):
        self.X = tf.placeholder("float", [None, self.n_inputs])
        self.Y = tf.placeholder("float", [None, self.n_outputs])
        self.weights = [None] * (len(self.n_hiddens) + 1)
        self.bias = [None] * (len(self.n_hiddens) + 1)
        for i in range(len(self.n_hiddens)):
            if (i == 0):
                self.weights[i] = tf.Variable(tf.random_normal([self.n_inputs, self.n_hiddens[i]]), name="weights_" + str(i))
            else:
                self.weights[i] = tf.Variable(tf.random_normal([self.n_hiddens[i - 1], self.n_hiddens[i]]), name="weights_" + str(i))
        self.weights[len(self.n_hiddens)] = tf.Variable(tf.random_normal([self.n_hiddens[len(self.n_hiddens) - 1], self.n_outputs]), name="weights_" + str(i))
        for i in range(len(self.bias) - 1):
            self.bias[i] = tf.Variable(tf.zeros([self.n_hiddens[i]]), name="bias_" + str(i))
        self.bias[len(self.bias) - 1] = tf.Variable(tf.zeros([self.n_outputs]), name="bias_" + str(len(self.bias) - 1))
        self.session = tf.Session()

        self.session.run(tf.global_variables_initializer())
        self.writer = tf.summary.FileWriter('Libs/LogsTF', self.session.graph)

        # Creating tensors
        self.forward = self.create_forward()
        self.cost = cost = tf.reduce_mean(-self.Y * tf.log(self.forward) - (1 - self.Y) * tf.log(1 - self.forward))
        # Change here the optimizer later for experimentations
        self.optimizer = tf.train.GradientDescentOptimizer(learning_rate=self.learning_rate).minimize(self.cost)

    def create_forward(self):
        output = [None] * (len(self.n_hiddens) + 1)
        #first = tf.sigmoid(tf.matmul([input], self.weights[0]) + self.bias[0])
        output[0] = tf.sigmoid(tf.matmul(self.X,self.weights[0]) + self.bias[0])
        for i in range(1, len(self.n_hiddens) + 1):
            output[i] = tf.sigmoid(tf.matmul(output[i - 1], self.weights[i]) + self.bias[i])

        return output[len(self.n_hiddens)]

    def load_weights(self, filename):
        return 0

    def save_weights(self, filename):
        return 0

    def train(self, input, output):
        self.session.run(self.optimizer, feed_dict={self.X: [input], self.Y: [output]})
        return self.session.run(self.cost, feed_dict={self.X: [input], self.Y: [output]})

    def guess(self, input):
        return self.session.run(self.forward, feed_dict={self.X: [input]})


"""
    Testing to resolve a xor to test the class
"""

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
