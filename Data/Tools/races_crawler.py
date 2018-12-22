"""
    /!\ Dangerous area /!\
    This script downloads races from programmes json data in 'Raw' folder.
    It's directly connecting to PMU servers ! So be really carefull with timing !
    Each 'programme' contains all races for the day. We only bet on 'plat' races, cause they're the most expectables.
"""

import os
import json
import time
import requests

def write(name, content):
    with open('/home/tom/Documents/Programmation/Python/OpenBet/Data/RacesRaw/race_' + name + '.json', 'w+') as file:
        file.write(content)

URL = "https://tablette.turfinfo.api.pmu.fr/rest/client/1/programme/{}/R{}/C{}/participants"
error_number = 0
race_number = 0

for filename in os.listdir('/home/tom/Documents/Programmation/Python/OpenBet/Data/ProgrammesRaw'):
     with open('/home/tom/Documents/Programmation/Python/OpenBet/Data/ProgrammesRaw/' + filename) as file:

         date = filename.split('_')[1].split(".")[0]

         day = json.loads(file.read())

         # We got multiple events on the day
         for event_n, event in enumerate(day["programme"]["reunions"]):
             field_id = event["hippodrome"]["code"]

             # We got multiple races for each event
             for race_n, race in enumerate(event["courses"]):

                 if (race['discipline'] == "PLAT"):
                     if ("ordreArrivee" in race and "corde" in race and "distance" in race):
                         result = race["ordreArrivee"]
                         rope = race["corde"]
                         distance = race["distance"]
                         # We generate the URL of the race
                         url = URL.format(date, event_n + 1, race_n + 1)
                         race_number += 1
                         #print(url)

                         name = date + "_R" + str(event_n + 1) + "C" + str(race_n + 1)
                         r = requests.get(url)
                         write(name, r.text)
                         time.sleep(5)

                         print((race_number / 6397 * 100), "%")

                     else:
                         error_number += 1

print(error_number, "errors")
print(race_number, "races")
