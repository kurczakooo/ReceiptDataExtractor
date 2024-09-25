import numpy as np
import os
import pandas as pd


list = os.listdir('results//')

for i in range(len(list)):
    list[i] = os.path.join('results//', list[i])

validation = list[-1]
tests = list[:-1]


with open(validation, 'r', encoding='utf-8') as f:
    ground_truth = f.read()
    f.close()
    
print(ground_truth)

"""replace_dic = {261 : 97,
    281 : 101,
    263 : 99,
    347 : 115,
    380 : 122,
    378 : 122,
    322 : 108,
    243 : 111}"""