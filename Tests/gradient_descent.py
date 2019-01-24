import numpy as np

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

n_i = 2
n_h = 500
n_o = 1

lr = 0.1

w1 = np.random.randn(n_h, n_i)
b1 = np.random.randn(n_h, 1)
w2 = np.random.randn(n_o, n_h)
b2 = np.random.randn(n_o, 1)

def forward(input):
    Z1 = np.matmul(w1, np.transpose(np.array([input]))) + b1
    A1 = sigmoid(Z1)
    Z2 = np.matmul(w2, A1) + b2
    A2 = sigmoid(Z2)
    return (A1, A2)

def cost(inputs, targets):
    sum = 0
    for i in range(len(inputs)):
        pred = forward(inputs[i])[-1][0][0]
        target = targets[i][0]
        sum += (target * np.log(pred) + (1 - target) * np.log(1 - pred))
    return (-1 / len(inputs)) * sum

def train(inputs, targets):
    pred = forward(inputs)

    dZ2 = pred[-1] - targets
    dW2 = np.dot(dZ2, np.transpose(pred[0]))
    dB2 = np.sum(dZ2, axis=1, keepdims=True)

    dZ1 = np.multiply( np.dot(np.transpose(w2), dZ2), 1 - np.power(pred[0], 2))
    dW1 = np.dot(dZ1, [inputs])
    dB1 = np.sum(dZ1, axis=1, keepdims=True)

    '''
    w1 = w1 - lr * dW1
    w2 = w2 - lr * dW2
    b1 = b1 - lr * dB1
    b2 = b2 - lr * dB2
    '''
    return (dW1, dW2, dB1, dB2)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


for i in range(1000):
    (dW1, dW2, dB1, dB2) = train(x_train[i % 4], y_train[i % 4])
    w1 = w1 - lr * dW1
    w2 = w2 - lr * dW2
    b1 = b1 - lr * dB1
    b2 = b2 - lr * dB2
    print(cost(x_train, y_train))


for i in range(len(x_train)):
    print(forward(x_train[i])[-1][0] )
