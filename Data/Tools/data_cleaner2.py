import os
import math
import json
import numpy as np
import random

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"


total = len(os.listdir(PATH + "../ProgrammesRaw/"))

n = 0
errors = 0

a = 0
b = 0

races = []

def process_course(course, reunion, course_n, date):
    filename = PATH + "../RacesRaw/race_" + date + "_R" + str(course["numReunion"]) + "C" + str(course_n) + ".json"

    if (os.path.isfile(filename)):
        with open(filename) as course_file:
            c = json.loads(course_file.read())
            if ("participants" in c):

                runners = []

                for p in c["participants"]:
                    if ("statut" in p):
                        if (p["statut"] == "PARTANT"):
                            if ("race" in p and "placeCorde" in p and "driver" in p and "driverChange" in p and "indicateurInedit" in p and "musique" in p and "handicapPoids" in p and "ordreArrivee" in p):

                                #odd = 8.52
                                if ("dernierRapportDirect" in p):
                                    odd = p["dernierRapportDirect"]["rapport"]
                                else:
                                    #odd = -1
                                    odd = 20 + (random.random() - 0.5) * 8

                                n_courses = 0
                                if ("nombreCourses" in p):
                                    n_courses = p["nombreCourses"]

                                gainsCarriere = 0
                                if ("gainsParticipant" in p):
                                    if ("gainsCarriere" in p["gainsParticipant"]):
                                        gainsCarriere = p["gainsParticipant"]["gainsCarriere"]

                                runners.append({
                                    'race': p["race"],
                                    'row': p["placeCorde"],
                                    'handicap': p["handicapPoids"],
                                    'gains': gainsCarriere,
                                    'race_numbers': n_courses,
                                    'driver': p["driver"],
                                    'driver_change': p["driverChange"],
                                    'first_race': p["indicateurInedit"],
                                    'musique': p["musique"],
                                    'standing': p["ordreArrivee"],
                                    'odd': odd
                                })

                if ("corde" in course and "montantTotalOffert" in course and "nature" in reunion and "hippodrome" in reunion and "distance" in course):
                    name = "R" + str(course["numReunion"]) + "C" + str(course_n)
                    return {
                        'date': date,
                        'name': name,
                        'nature': reunion["nature"],
                        'stadium': reunion["hippodrome"]["code"],
                        'distance': course["distance"],
                        'reward': course["montantTotalOffert"],
                        'corde': course["corde"],
                        'runners': runners
                    }
                else:
                    return -1
            else:
                return -1
    else:
        return -1

# We loop through all programmes
for programme_file in os.listdir(PATH + "../ProgrammesRaw/"):
    n+=1

    with open(PATH + "../ProgrammesRaw/" + programme_file) as programme:
        p = json.loads(programme.read())
        date = programme_file.split("_")[1].split(".")[0]

        if ("programme" in p):
            if ("reunions" in p["programme"]):
                for r in p["programme"]["reunions"]:
                    if ("courses" in r):
                        courses_n = len(r["courses"])
                        for i in range(courses_n):
                            if (r["courses"][i]["discipline"] == "PLAT"):
                                race = process_course(r["courses"][i], r, i+1, date)
                                if (race == -1):
                                    errors += 1
                                else:
                                    races.append(race)

                    else:
                        errors += 1

            else:
                errors += 1
        else:
            errors += 1


    print(math.floor(n / total * 10000) / 100, "%")

print("Done,", errors, "errors,", len(races), "races generated, saving file...")

with open(PATH + "../dataset.json", "w+") as file:
    file.write(json.dumps(races))
