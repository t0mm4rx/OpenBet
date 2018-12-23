"""
    Data fetching tools. Set of functions.
        - get_day_races (date (str)): returns all races for the given day
        - get_race (date (str), name (str)): returns a race with given parameters. Example of name: 'R1C1'. Example of date: '23112018'.
        - get_all_races_names (): returns list of object containing date and name of all races downloaded
        - get_all_races (): returns list of all downloaded races. /!\ Slow function /!\
        - get_jockey_id (jockey_name (str)): returns id of jockey with given name
        - get_horse_id (horse_name (str)): returns id of horse with given name
        - get_jockey_name (jockey_id (int)): returns jockey name corresponding to given id
        - get_horse_name (jockey_id (int)): returns horse name corresponding to given id
        - get_field_id (field_code (str)): returns id of field with given code
        - get_horse_races (horse_id (int)): returns all races ran by given horse
        - get_jockey_races (jockey_id (int)): returns all races ran by given jockey
"""

import json
import os
import time

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

def get_all_races_names():
    result = []
    for filename in os.listdir(PATH + '../Data/Races/'):
        date = filename.split("_")[1]
        name = filename.split("_")[2].split(".")[0]
        result.append({ 'date': date, 'name': name })
    return result


def get_all_races():
    names = get_all_races_names()
    result = []
    for name in names:
        result.append(get_race(name["date"], name["name"]))
    return result

def get_horse_id(horse_name):
    for id in data_horse_id:
        if (id["code"] == horse_name):
            return id["id"]

def get_jockey_id(jockey_name):
    for id in data_jockey_id:
        if (id["code"] == jockey_name):
            return id["id"]

def get_field_id(field_code):
    for id in data_field_id:
        if (id["code"] == field_code):
            return id["id"]

def get_horse_races(horse_id):
    result = []
    for race in data_races:
        for runner in race["participants"]:
            if (get_horse_id(runner["nom"]) == horse_id):
                result.append(race)
    return result

def get_jockey_races(jockey_id):
    result = []
    for race in data_races:
        for runner in race["participants"]:
            if ("driver" in runner):
                if (get_jockey_id(runner["driver"]) == jockey_id):
                    result.append(race)
    return result

def get_jockey_name(jockey_id):
    for id in data_jockey_id:
        if (id["id"] == jockey_id):
            return id["code"]

def get_horse_name(horse_id):
    for id in data_horse_id:
        if (id["id"] == horse_id):
            return id["code"]

"""
    Loading data in memory to fasten access later (about 170Mo of data per year downloaded).
"""
start = time.clock()
print("Loading data (races + id)...")
data_races = get_all_races()
data_horse_id = json.loads(open(PATH + "../Data/Id/horses.json").read())
data_jockey_id = json.loads(open(PATH + "../Data/Id/jockeys.json").read())
data_field_id = json.loads(open(PATH + "../Data/Id/fields.json").read())
print("Data successfully loaded in", round(time.clock() - start, 1), "seconds")
