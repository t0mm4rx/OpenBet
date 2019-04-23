import os
import json
import matplotlib.pyplot as plt
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

data = []

with open(PATH + "../dataset.json") as file:
    a = json.loads(file.read())
    print("File loaded")

    for race in a:
        data.append(len(race['runners']))

plt.hist(data)
plt.savefig(PATH + "Outputs/runners_n.png")
