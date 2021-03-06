import os
import json
import math
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

natures = []

total = len(os.listdir(PATH + '../ProgrammesRaw'))
n = 0
for filename in os.listdir(PATH + '../ProgrammesRaw'):
    with open(PATH + '../ProgrammesRaw/' + filename) as file:
        n += 1
        a = json.loads(file.read())
        if ("programme" in a):
            for b in a["programme"]["reunions"]:
                if (not b['nature'] in natures):
                    natures.append(b['nature'])
        print(math.floor(n / total * 100), "%")

print()
print(natures)
