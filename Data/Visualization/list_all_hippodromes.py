import os
import json
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

hippodromes = []

total = len(os.listdir(PATH + '../ProgrammesRaw'))
n = 0
for filename in os.listdir(PATH + '../ProgrammesRaw'):
    with open(PATH + '../ProgrammesRaw/' + filename) as file:
        n += 1
        a = json.loads(file.read())
        if ("programme" in a):
            for b in a["programme"]["reunions"]:
                if (not b['hippodrome']["code"] in hippodromes):
                    hippodromes.append(b['hippodrome']["code"])
        print(n / total * 100, "%")

print()
print(hippodromes)
