import tensorflow as tf
from matplotlib import pyplot as plt
import random
import time

# Hyperparameters
TOTAL_EXAMPLES = 100
ITERS = 1000
BATCH_SIZE = 1
LEARNING_RATE = 0.1

# Dataset
x1 = [0] * TOTAL_EXAMPLES
x2 = [0] * TOTAL_EXAMPLES
x1 = list(x1)
x2 = list(x2)
y = [0] * TOTAL_EXAMPLES
y = list(y)

for i in range(TOTAL_EXAMPLES):
    x1[i] = random.randint(0, 30)
    x2[i] = random.randint(0, 30)
    if (x2[i] + x1[i] > 30):
        y[i] = 1
    else:
        y[i] = 0

# Feature scaling
max_x1 = max(x1)
max_x2 = max(x2)
for i in range(len(x1)):
    x1[i] = float(float(x1[i]) / max_x1)
    x2[i] = float(float(x2[i]) / max_x2)

for i in range(len(x1)):
    if (y[i] == 1):
        plt.scatter(x1[i], x2[i], c='red')
    else:
        plt.scatter(x1[i], x2[i], c='blue')

plt.show()

# ML - TF vars
thetas = tf.Variable(tf.zeros([3, 1], tf.float32), name="thetas")
inputs = tf.placeholder(tf.float32, shape=(None, 3))
target = tf.placeholder(tf.float32, shape=(None, 1))

prediction = tf.sigmoid(tf.matmul(inputs, thetas))

a = tf.multiply( tf.multiply(-1.0, target), tf.log(tf.add(prediction, 0.0000001)) )
b = tf.multiply( tf.subtract(1.0, target), tf.log( tf.subtract(1.0000001, prediction) ) )
cost = tf.divide( tf.reduce_sum(tf.subtract(a, b)), BATCH_SIZE)

#cost = tf.reduce_sum(tf.square(tf.subtract(target, prediction)))
#optimizer = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cost)

gradients = tf.divide(tf.matmul( tf.transpose(inputs), tf.subtract(prediction, target) ), BATCH_SIZE)
correct_gradients = tf.assign(thetas, tf.add( thetas, tf.multiply(-LEARNING_RATE, gradients) ))

# ML - Executing
session = tf.Session()
tf.summary.scalar('cost', cost)
merged = tf.summary.merge_all()
train_writer = tf.summary.FileWriter( './TFLogs/run' + str(time.time()), session.graph)

session.run(tf.global_variables_initializer())


trainingset_x = [[0]] * BATCH_SIZE
trainingset_y = [[0]] * BATCH_SIZE
for x in range(BATCH_SIZE):
    trainingset_x[x] = [1.0, x1[x], x2[x]]

for x in range(BATCH_SIZE):
    trainingset_y[x] = [y[x]]

for i in range(ITERS):
    session.run(correct_gradients, feed_dict={inputs: trainingset_x, target: trainingset_y})
    print(session.run(cost, feed_dict={inputs: trainingset_x, target: trainingset_y}))
    summary, acc = session.run([merged, cost], feed_dict={inputs: trainingset_x, target: trainingset_y})
    train_writer.add_summary(summary, i)

print(thetas.eval(session=session))

"""
for i in range(10000):

    trainingset_x = [[0]] * BATCH_SIZE
    trainingset_y = [[0]] * BATCH_SIZE
    for x in range(BATCH_SIZE):
        trainingset_x[x] = [1.0, x1[i % 25 + x], x2[i % 25 + x]]

    for x in range(BATCH_SIZE):
        trainingset_y[x] = [y[i % 25 + x]]


    #session.run(optimizer, feed_dict={inputs: trainingset_x, target: trainingset_y})
    #print(session.run(cost, feed_dict={inputs: trainingset_x, target: trainingset_y}))
    summary, acc = session.run([merged, cost], feed_dict={inputs: trainingset_x, target: trainingset_y})
    train_writer.add_summary(summary, i)

#print(session.run(prediction, feed_dict={inputs: trainingset_x, target: trainingset_y}))

"""
train_writer.close()
