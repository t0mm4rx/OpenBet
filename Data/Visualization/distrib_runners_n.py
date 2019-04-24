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

print("7", data.count(7))
print("8", data.count(8))
print("9", data.count(9))
print("10", data.count(10))
print("11", data.count(11))
print("12", data.count(12))
