"""
    Each field, horse and jockey needs to have an id. So we generate it in this file.
"""

import sys
sys.path.insert(0, 'Libs')

import os
import data_fetcher
import json

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
field_ids = []
horse_ids = []
jockey_ids = []

field_last_id = 0
horse_last_id = 0
jockey_last_id = 0

def is_id_existing(array, code):
    for el in array:
        if (el["code"] == code):
            return True
    return False

def write(name, content):
    with open(PATH + '../Id/' + name + '.json', 'w+') as file:
        file.write(content)

races = data_fetcher.get_all_races()

for race_infos in races:
    race = data_fetcher.get_race(race_infos['date'], race_infos['name'])
    """
    if (not is_id_existing(field_ids, race['terrain_id'])):
        field_ids.append({ 'code':  race['terrain_id'], 'id': field_last_id})
        field_last_id += 1
    """
    for runner in race['participants']:
        """
        if (not is_id_existing(horse_ids, runner["nom"])):
            horse_ids.append({ 'code':  runner["nom"], 'id': horse_last_id})
            horse_last_id += 1
        """
        if ("driver" in runner):
            if (not is_id_existing(jockey_ids, runner["driver"])):
                jockey_ids.append({ 'code':  runner["driver"], 'id': jockey_last_id})
                jockey_last_id += 1
        #exit()

#write('fields', json.dumps(field_ids))
#write('horses', json.dumps(horse_ids))
write('jockeys', json.dumps(jockey_ids))
