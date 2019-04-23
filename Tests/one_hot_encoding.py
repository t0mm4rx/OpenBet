import sys
import os
import random
import numpy as np

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(PATH + '../')

import json
from Libs import data_converter

print(data_converter.one_hot_encoding(2, 4))
print(data_converter.race("ANGLO ARABE"))
print(data_converter.row(25))
print(data_converter.nature("SEMINOCTURNE"))
print(data_converter.stadium("FEU"))
