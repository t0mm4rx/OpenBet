"""
    Data fetching tools. Set of functions.
        - get_day_races (date (str)): returns all races for the given day
        - get_race (date (str), name (str)): returns a race with given parameters. Example of name: 'R1C1'. Example of date: '23112018'.
"""

import json
import os

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

def get_race(date, name):
    with open(PATH + "../Data/Races/race_" + date + "_" + name + ".json") as file:
        return json.loads(file.read())

def get_day_races(date):
    result = []
    for filename in os.listdir(PATH + '../Data/Races/'):
        if (date in filename):
            with open(PATH + "../Data/Races/" + filename) as file:
                result.append(json.loads(file.read()))
    return result

def get_all_races():
    result = []
    for filename in os.listdir(PATH + '../Data/Races/'):
        date = filename.split("_")[1]
        name = filename.split("_")[2].split(".")[0]
        result.append({ 'date': date, 'name': name })
    return result


#print(get_race("01012018", "R3C1"))
#print(get_day_races("01012018"))
