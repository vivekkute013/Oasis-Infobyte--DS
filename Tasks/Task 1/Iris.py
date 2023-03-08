# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:14:39 2023

@author: Vivek
"""

#  Iris Flower Classification

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('D:\Machine Learning\LGM\Task 1/iris.data')
x = dataset.iloc[:,: -1].values
y = dataset.iloc[:,4].values
y = np.reshape(y,(149,1))

# converting string to numeric 
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
y[:,0] = LE.fit_transform(y)

# Using Random Forest regression
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor()
reg.fit(x,y)

Prediction = reg.predict([[4.8,3.0,1.4,0.1]])
if(Prediction[0] == 0):
    print("Iris - Setosa")
elif(Prediction[0] == 1):
    print("Iris - Versicolor")
else:
    print("Iris - Vergoinica")



