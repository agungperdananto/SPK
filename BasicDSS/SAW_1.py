# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:57:12 2019

@author: Agung Perdananto
"""

# import libraries
import pandas as pd
import numpy as np
dataset = pd.read_csv('data_2.csv')

dataset = np.array(dataset.values)
# label encoder
pendidikan = dataset[:,2]
pendidikan_ = []
for jenjang in pendidikan:
    if jenjang =='SMK':
        pendidikan_.append(0)
    elif jenjang =='S1':
        pendidikan_.append(1)
    else:
        pendidikan_.append(2)
    
print(pendidikan_)
dataset = np.array(dataset)
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

# SAW____Process
# Normalize matrix
x, y = dataset.shape
normalized_matrix = []
for i in range(x):
    normalized_row = []
    for j in range(y):
        if benefit[j]:
            normalized_row.append(dataset[i, j]/max(dataset[:,j]))
        else:
            normalized_row.append(min(dataset[:, j])/dataset[i, j])
    normalized_matrix.append(normalized_row)
    
normalized_matrix = np.array(normalized_matrix)

# Weighting and suming
results = []
for i in range(x):
    result = 0
    for j in range(y):
        result += normalized_matrix[i,j] * normalized_weight[j]
    results.append(round(result, 2))

results
















