import re
import numpy as np
import json
import os

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
races = ["PUR-SANG", "ANGLO ARABE DE COMPLEMENT", "ANGLO ARABE", "INCONNU", "AQPS",
         "ARABE", "CHEVAL DE SELLE", "CHEVAL DE SELLE FRANCAIS", "TROTTEUR FRANCAIS"]
natures = ['DIURNE', 'SEMINOCTURNE', 'NOCTURNE']
stadiums = ['ENG', 'D13', 'CHB', 'COM', 'PON', 'PAR', 'AMI', 'DEA', 'XKD', 'CAG', 'WOL', 'XGD', 'CEP', 'AVE', 'STR', 'VIL', 'CDM', 'CAP', 'NIM', 'ANG', 'GRA', 'BRI', 'CHA', 'HYE', 'PET', 'VIN', 'YON', 'FON', 'AUT', 'BEA', 'ROU', 'A24', 'HPV', 'HWM', 'D04', 'F20', 'LAV', 'D15', 'CAB', 'PLB', 'CHR', 'SIN', 'GAL', 'CAV', 'EVX', 'POM', 'BAD', 'KRK', 'MAC', 'DIE', 'SON', 'CHM', 'CRO', 'AIX', 'SYD', 'LFD', 'PCH', 'D93', 'ARG', 'SU1', 'PAU', 'KRI', 'MDF', 'STD', 'MXD', 'BGR', 'BOU', 'VIR', 'BOR', 'LYO', 'D01', 'DUB', 'FEU', 'LLA', 'TAR', 'CHL', 'GEL', 'BRA', 'LON', 'CHE', 'CHO', 'LSO', 'VIC', 'CAE', 'SAI', 'VIT', 'CRT', 'DUS', 'CRA', 'SSB', 'S88', 'HOP', 'MAR', 'H3D', 'AGE', 'D73', 'MAI', 'PUN', 'XTD', 'SIO', 'SAL', 'REI', 'VPR', 'G67', 'MAU', 'S85', 'GRE', 'MDM', 'LAT', 'ASC', 'KEM', 'BED', 'N74', 'RAM', 'LAO', 'AGL', 'AVI', 'LIS', 'S-M', 'S84', 'Q07', 'EPS', 'BEN', 'CLA', 'F16', 'F03', 'BER', 'SEN', 'SHT', 'MKT', 'DAX', 'MOU', 'TPK', 'B09', 'MAN', 'GOO', 'TOU', 'CHT', 'Q04', 'WVD', 'LAR', 'KOE', 'BJE', 'MSM', 'D08', 'SEG', 'O01', 'FRA', 'BOL', 'JUL', 'AUC', 'CRP', 'F9D', 'CAT', 'WIS', 'TRS', 'CAR', 'MAL', 'BVD', 'LPA', 'LIG', 'ABY', 'R97',
            'LJD', 'AXD', 'OST', 'G36', 'HAM', 'XCD', 'LEO', 'NAP', 'JBG', 'F18', 'VY3', 'MEA', 'S87', 'NIO', 'PIN', 'DUR', 'ORA', 'CRL', 'PID', 'CUR', 'MLN', 'MOR', 'VAN', 'VLR', 'AV2', 'D12', 'HAY', 'DIV', 'ZAD', 'E1D', 'D95', 'YOR', 'A10', 'COR', 'MSD', 'EAU', 'ZOZ', 'D02', 'D16', 'N80', 'KOU', 'ECO', 'MEG', 'YRD', 'B2D', 'D94', 'ALE', 'D23', 'SDW', 'E2D', 'PBD', 'JAG', 'VEL', 'MVY', 'D09', 'TOK', 'CAS', 'NBU', 'MON', 'MLT', 'RDW', 'D27', 'ERB', 'NMS', 'BAV', 'BRE', 'WAR', 'U09', 'STM', 'VSL', 'SOL', 'Q01', 'D14', 'BAL', 'ISL', 'FOU', 'COP', 'LAN', 'SSS', 'V98', 'LGC', 'AGC', 'SOM', 'AJA', 'G14', 'OSL', 'ROY', 'U19', 'MIL', 'CZD', 'WJD', 'A14', 'KUU', 'PDF', 'DON', 'A25', 'RPP', 'SHE', 'ZED', 'BUC', 'NSE', 'VTR', 'LDV', 'D21', 'CA2', 'F25', 'KIL', 'CAD', 'HXD', 'R8D', 'HOB', 'BSD', 'BIA', 'GPD', 'ARR', 'DE2', 'D87', 'BLG', 'AU2', 'EKS', 'Q02', 'EN2', 'I15', 'ZUR', 'D20', 'CHD', 'MIK', 'CPD', 'N9D', 'KSD', 'RMG', 'I04', 'MED', 'NGD', 'SJM', 'D18', 'HEL', 'ECH', 'I27', 'Z93', 'G9D', 'NSD', 'RED', 'G13', 'HRP', 'F26', 'G10', 'U14', 'SA7', 'S5D', 'QU1', 'DHD', 'LCY', 'CHX', 'WPD', 'G48', 'TOT', 'F21', 'RRD', 'BLA', 'N68', 'D06', 'CH2', 'ADT']


rows = list(range(1, 26))


def find_char(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i


def musique(musique):
    if (musique == '-'):
        return 5.72 / 11.0
    if (musique == 'Inédit'):
        return 5.72 / 11.0

    musique = re.sub("[\(\[].*?[\)\]]", "", musique)
    locs = list(find_char(musique, 'p'))

    pos = []
    for loc in locs:
        if (musique[loc - 1] == "T" or musique[loc - 1] == "A"):
            pos.append(0)
        elif (musique[loc - 1] == "D" or musique[loc - 1] == "R"):
            pos.append(6)
        else:
            pos.append(int(musique[loc - 1]))

    if (len(pos) > 0):
        score = 0
        for p in pos:
            if (p == 0):
                score += 11
            else:
                score += p
        return (score / len(pos)) / 11.0
    else:
        return 5.72 / 11.0


def handicap(handicap):
    return handicap / 790


def races_number(races):
    return races / 394


def distance(distance):
    return distance / 4300


def reward(reward):
    return reward / 13860216


def odd(odd):
    return odd / 735.7


def one_hot_encoding(value, values):
    arr = [0] * values
    arr[value] = 1
    return arr


def race(race):
    return one_hot_encoding(races.index(race), len(races))


def row(row):
    return one_hot_encoding(rows.index(row), len(rows))


def nature(nature):
    return one_hot_encoding(natures.index(nature), len(natures))


def driver_change(val):
    return int(val)


def first_race(val):
    return int(val)


def corde(corde):
    if (corde == "CORDE_GAUCHE"):
        return 1
    else:
        return 0


def stadium(stadium):
    return one_hot_encoding(stadiums.index(stadium), len(stadiums))


def targets(race):
    for i, runner in enumerate(race["runners"]):
        if (runner["standing"] == 1):
            return one_hot_encoding(i, len(race["runners"]))


def runner_features(runner):
    return np.hstack(np.array([
        np.array(race(runner["race"])),
        np.array(row(runner["row"])),
        handicap(runner["handicap"]),
        races_number(runner["race_numbers"]),
        driver_change(runner["driver_change"]),
        first_race(runner["first_race"]),
        musique(runner["musique"])
    ]))


def runner_features_odds(runner):
    return np.hstack(np.array([
        np.array(race(runner["race"])),
        np.array(row(runner["row"])),
        handicap(runner["handicap"]),
        races_number(runner["race_numbers"]),
        driver_change(runner["driver_change"]),
        first_race(runner["first_race"]),
        musique(runner["musique"]),
        odd(runner['odd'])
    ]))


def features(race):
    r = []
    for runner in race["runners"]:
        r.append(runner_features_odds(runner))

    return np.hstack(np.array([
        nature(race["nature"]),
        stadium(race["stadium"]),
        distance(race["distance"]),
        reward(race["reward"]),
        corde(race["corde"]),
        np.hstack(np.array(r))
    ]))


def filter_runners(limit, runners):
    n = 0
    res = []
    while (len(res) < limit):
        if (n > 10):
            break
        n += 1
        for x in runners:
            if (x['standing'] <= limit and not x in res):
                res.append(x)
                break
    return res

def get_dataset():
    f = []
    t = []
    o = []
    with open(PATH + '../Data/dataset.json') as file:
        a = json.loads(file.read())

        for r in a:
            if (len(r['runners']) >= 8):
                c = r
                c['runners'] = filter_runners(8, r['runners'])

                if (len(np.array(targets(c)).shape) > 0 and len(c['runners']) == 8):
                    f.append(np.array(features(c)))
                    t.append(np.array(targets(c)))
                    for p in c["runners"]:
                        if (p["standing"] == 1):
                            o.append(p['odd'])
    return f, t, o
