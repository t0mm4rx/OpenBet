import os
import json
import matplotlib.pyplot as plt
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

data = []

with open(PATH + "../dataset.json") as file:
    a = json.loads(file.read())
    print("File loaded")

    for race in a:
        for d in race['runners']:
            data.append(d['odd'])

plt.hist(data, list(range(40)))
plt.savefig(PATH + "Outputs/gains.png")
