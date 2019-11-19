# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:28:02 2019

@author: Agung Perdananto
"""

# import libraries
import pandas as pd
import numpy as np
dataset = pd.read_csv('data_2.csv')
dataset = np.array(dataset)

# label encoder
pendidikan = dataset[:,2]
pendidikan_ = []
for jenjang in pendidikan:
    if jenjang =='SMK':
        pendidikan_.append(1)
    elif jenjang =='S1':
        pendidikan_.append(2)
    else:
        pendidikan_.append(3)

dataset[:,2] = pendidikan_
print(dataset)

# create weight
weight = [3,4,3,4,4]
normalized_weight = []
for w in weight:
    normalized_weight.append(round(w/sum(weight), 2))
normalized_weight
sum(normalized_weight)
# define criteria
benefit = [True, False, True, False, True]
x, y = dataset.shape
results = []
for i in range(x):
    value = 1
    for j in range(y):
        if benefit[j]:
            value *= dataset[i, j] ** normalized_weight[j]
        else:
            value *= dataset[i, j] ** (-1*normalized_weight[j])
    results.append(round(value, 2))

final = []
for result in results:
    final.append(round(result/sum(results),2))

final






