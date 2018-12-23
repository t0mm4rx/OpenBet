import sys
sys.path.insert(0, 'Libs')

import data_fetcher

print(len(data_fetcher.get_day_races("01012018")))
print(len(data_fetcher.get_race("01012018", "R3C1")))
