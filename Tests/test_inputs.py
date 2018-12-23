import sys
sys.path.insert(0, 'Libs')

import data_fetcher
import inputs_generator


for race in data_fetcher.data_races:
    for runner in race['participants']:
        print(inputs_generator.runner_to_input(runner, race))
