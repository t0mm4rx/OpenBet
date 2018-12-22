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

class NeuralNetwork:

    def __init__(self, n_inputs, n_hidden, n_output):
        self.n_inputs = n_inputs
        self.n_hidden = n_hidden
        self.n_outputs = n_outputs

    def load_weights(self, filename):
        return 0

    def save_weights(self, filename):
        return 0

    def train(self, input, output):
        return 0

    def guess(self, input):
        return 0
