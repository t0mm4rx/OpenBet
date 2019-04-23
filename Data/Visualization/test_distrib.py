import matplotlib.pyplot as plt
import numpy as np
import os

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

data = np.random.normal(5, 1, 1000)
#print(data)

plt.hist(data)
plt.savefig(PATH + "Outputs/hist.png")
