"""
    This script cleans the previous downloaded data : programmes and races.
    It creates a clean object for each race and saves it as json.
"""

import os
import json
import time
import requests


def write(name, content):
    with open('/home/tom/Documents/Programmation/Python/OpenBet/Data/Races/race_' + name + '.json', 'w+') as file:
        file.write(content)


TOTAL_RACES = 6398

total = 0
errors = 0

for filename in os.listdir('/home/tom/Documents/Programmation/Python/OpenBet/Data/ProgrammesRaw'):
    with open('/home/tom/Documents/Programmation/Python/OpenBet/Data/ProgrammesRaw/' + filename) as file:

        date = filename.split('_')[1].split(".")[0]

        day = json.loads(file.read())

        # We got multiple events on the day
        for event_n, event in enumerate(day["programme"]["reunions"]):
            field_id = event["hippodrome"]["code"]
            nature = event["nature"]
            audience = event["audience"]
            if ("meteo" in event):
                weather = event["meteo"]
            else:
                weather = {}

            # We got multiple races for each event
            for race_n, race in enumerate(event["courses"]):

                if (race['discipline'] == "PLAT"):
                    if ("ordreArrivee" in race and "corde" in race and "distance" in race):
                        name = date + "_R" + str(event_n + 1) + "C" + str(race_n + 1)
                        with open('/home/tom/Documents/Programmation/Python/OpenBet/Data/RacesRaw/race_' + name + '.json') as file:
                            runners = json.loads(file.read())
                            if ("participants" in race and "participants" in runners):
                                race["participants"] = runners["participants"]
                                race["date"] = date
                                race["nom"] = "R" + str(event_n + 1) + "C" + str(race_n + 1)
                                race["terrain_id"] = field_id
                                race["meteo"] = weather
                                race["audience"] = audience
                                race["nature"] = nature
                                write(name, json.dumps(race))

                                total += 1
                            else:
                                errors += 1
                    print(str((errors + total) / TOTAL_RACES * 100), "%")


print("Total", total)
print("Errors", errors)
