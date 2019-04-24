import sys
import os
import random
import numpy as np
import json

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(PATH + '../')

from Libs import betting_tools


print(betting_tools.get_gain(8.52, False))
