"""
    This file contains functions to convert dataset data in raw values for neural network processing.
        - standing_to_output(standing (int)): convert the standing of the runner in output for the nn
        - normalize_[datatype] (data): transform a data type into a float in range [-1; 1]
        - runner_to_input (runner (runner object)): takes as argument a runner object talen from the dataset, returns an array of normalized values ready to feed a nn
"""

import re

def standing_to_output(standing):
    if (standing == 1):
        return [1.0, 0.0, 0.0]
    elif (standing == 2):
        return [0.0, 1.0, 0.0]
    elif (standing == 3):
        return [0.0, 0.0, 1.0]
    else:
        return [0.0, 0.0, 0.0]

def normalize_bool(value):
    if (value):
        return 1.0
    else:
        return 0.0

def normalize_number(value, max):
    if (value > max):
        return max
    else:
        return round(value / max, 4)

def normalize_musique(musique):
    if ("Inédit" in musique):
        return 5.0

    musique = re.sub(r'\([^)]*\)', '', musique)
    standings = musique.split("p")
    average = 0
    count = 0
    for i in standings:
        if (i != '' and i.isdigit()):
            if (int(i) > 9 or int(i) == 0):
                average += 11.0
            else:
                average += int(i)
            count += 1
    if (count != 0):
        return round(1 / (average / count), 4)
    else:
        return 5.0

def normalize_trend(trend):
    if (trend == "+"):
        return 1.0
    elif (trend == "-"):
        return -1.0
    else:
        return 0.0

"""
    Important function, defines every data used in the neural network.
    Order in which we add the data is critical, so don't change it after training.
"""
def runner_to_input(runner, race):
    inputs = []

    """
        Runner based inputs
    """

    if ("handicapValeur" in runner):
        inputs.append(normalize_number(runner['handicapValeur'], 100.0))
    else:
        inputs.append(normalize_number(0.0, 100.0))

    if ("musique" in runner):
        inputs.append(normalize_musique(runner['musique']))
    else:
        inputs.append(normalize_musique("5p"))

    if ("jumentPleine" in runner):
        inputs.append(normalize_bool(runner['jumentPleine']))
    else:
        inputs.append(normalize_bool(False))

    if ("placeCorde" in runner):
        inputs.append(normalize_number(runner['placeCorde'], 24.0))
    else:
        inputs.append(normalize_number(12.0, 24.0))

    if ("age" in runner):
        inputs.append(normalize_number(runner['age'], 7.0))
    else:
        inputs.append(normalize_number(4.0, 7.0))

    if ("nombreCourses" in runner):
        inputs.append(normalize_number(runner['nombreCourses'], 30.0))
    else:
        inputs.append(normalize_number(5.0, 30.0))

    if ("nombreVictoires" in runner):
        inputs.append(normalize_number(runner['nombreVictoires'], 30.0))
    else:
        inputs.append(normalize_number(0.0, 30.0))

    if ("indicateurInedit" in runner):
        inputs.append(normalize_bool(runner['indicateurInedit']))
    else:
        inputs.append(normalize_bool(False))

    if ("dernierRapportDirect" in runner and "favoris" in runner["dernierRapportDirect"]):
        inputs.append(normalize_bool(runner["dernierRapportDirect"]['favoris']))
    else:
        inputs.append(normalize_bool(False))

    if ("dernierRapportDirect" in runner and "indicateurTendance" in runner["dernierRapportDirect"]):
        inputs.append(normalize_trend(runner["dernierRapportDirect"]['indicateurTendance']))
    else:
        inputs.append(normalize_trend(''))

    if ("dernierRapportDirect" in runner and "rapport" in runner["dernierRapportDirect"]):
        inputs.append(normalize_number(runner["dernierRapportDirect"]['rapport'], 50.0))
    else:
        inputs.append(normalize_number(5.0, 50.0))

    if ("nombrePlaces" in runner):
        inputs.append(normalize_number(runner['nombrePlaces'], 24.0))
    else:
        inputs.append(normalize_number(10.0, 24.0))

    if ("dernierRapportDirect" in runner and "nombreIndicateurTendance" in runner["dernierRapportDirect"]):
        inputs.append(normalize_number(runner["dernierRapportDirect"]['nombreIndicateurTendance'], 50.0))
    else:
        inputs.append(normalize_number(0.0, 50.0))

    if ("engagement" in runner):
        inputs.append(normalize_bool(runner['engagement']))
    else:
        inputs.append(normalize_bool(False))

    if ("driverChange" in runner):
        inputs.append(normalize_bool(runner['driverChange']))
    else:
        inputs.append(normalize_bool(False))

    if ("numPmu" in runner):
        inputs.append(normalize_number(runner['numPmu'], 24.0))
    else:
        inputs.append(normalize_number(False, 24.0))

    """
        Race based inputs
    """
    if ("montantTotalOffert" in race):
        inputs.append(normalize_number(race['montantTotalOffert'], 1000000.0))
    else:
        inputs.append(normalize_number(10000.0, 1000000.0))

    if ("nombreDeclaresPartants" in race):
        inputs.append(normalize_number(race['nombreDeclaresPartants'], 24.0))
    else:
        inputs.append(normalize_number(8.0, 24.0))

    if ("distance" in race):
        inputs.append(normalize_number(race['distance'], 5000.0))
    else:
        inputs.append(normalize_number(1500.0, 5000.0))

    if ("meteo" in race and "forceVent" in race["meteo"]):
        inputs.append(normalize_number(race["meteo"]['forceVent'], 100.0))
    else:
        inputs.append(normalize_number(10.0, 100.0))

    if ("meteo" in race and "temperature" in race["meteo"]):
        inputs.append(normalize_number(race["meteo"]['temperature'], 40.0))
    else:
        inputs.append(normalize_number(16.0, 40.0))

    return inputs
