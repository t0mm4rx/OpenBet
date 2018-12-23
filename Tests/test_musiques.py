import sys
sys.path.insert(0, 'Libs')

import data_fetcher
import inputs_generator

"""
for race in data_fetcher.data_races:
    for runner in race['participants']:
        print(inputs_generator.normalize_musique(runner["musique"]))
"""
for race in data_fetcher.data_races:
    for runner in race['participants']:
        if ("dernierRapportDirect" in runner and "indicateurTendance" in runner["dernierRapportDirect"]):
            print(runner["dernierRapportDirect"]["indicateurTendance"])
