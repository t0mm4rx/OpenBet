import os
import json
import math
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

horses = []

total = len(os.listdir(PATH + '../RacesRaw'))

n = 0
errors = 0
for filename in os.listdir(PATH + '../RacesRaw'):
    with open(PATH + '../RacesRaw/' + filename) as file:
        n += 1
        a = json.loads(file.read())
        if ("participants" in a):
            for b in a["participants"]:
                if (not b['nom'] in horses):
                    horses.append(b['nom'])
        else:
            errors += 1
        print(math.floor(n / total * 100), "%\r")

print("Errors:", errors / total * 100, "%")
print()
#print(horses)
with open(PATH + "Outputs/horses.json", "w+") as file:
    file.write(json.dumps(horses))
