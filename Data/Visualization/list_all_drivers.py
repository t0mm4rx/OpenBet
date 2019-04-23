import os
import json
import math
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

drivers = []

total = len(os.listdir(PATH + '../RacesRaw'))

n = 0
errors = 0
for filename in os.listdir(PATH + '../RacesRaw'):
    with open(PATH + '../RacesRaw/' + filename) as file:
        n += 1
        a = json.loads(file.read())
        if ("participants" in a):
            for b in a["participants"]:
                if ("driver" in b):
                    if (not b['driver'] in drivers):
                        drivers.append(b['driver'])
                else:
                    errors += 1
        else:
            errors += 1
        print(math.floor(n / total * 100), "%\r")

print("Errors:", errors / total * 100, "%")
print()
#print(horses)
with open(PATH + "Outputs/drivers.json", "w+") as file:
    file.write(json.dumps(drivers))
