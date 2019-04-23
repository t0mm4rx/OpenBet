import os
import json
import sys
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

sys.path.append(PATH + '../../')
from Libs import data_converter
import matplotlib.pyplot as plt


# Runner
max_handicap = 0
max_races = 0
max_gains = 0
max_row = 0

# Race
max_distance = 0
max_reward = 0

with open(PATH + "../dataset.json") as file:
    a = json.loads(file.read())

    for race in a:
        if (race["distance"] > max_distance):
            max_distance = race["distance"]
        if (race["reward"] > max_reward):
            max_reward = race["reward"]

        for runner in race["runners"]:
            if (runner['handicap'] > max_handicap):
                max_handicap = runner['handicap']
            if (runner['gains'] > max_gains):
                max_gains = runner['gains']
            if (runner['race_numbers'] > max_races):
                max_races = runner['race_numbers']
            if (runner['row'] > max_row):
                max_row = runner['row']

print("Max handicap", max_handicap)
print("Max gains", max_gains)
print("Max races", max_races)
print("Max distance", max_distance)
print("Max reward", max_reward)
print("Max row", max_row)
