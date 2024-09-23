import numpy as np
import os
import pandas as pd


list = os.listdir('results//')

for i in range(len(list)):
    list[i] = os.path.join('results//', list[i])

validation = list[-1]
tests = list[:-1]


