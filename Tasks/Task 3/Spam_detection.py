# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:16:53 2023

@author: Vivek
"""

# Spam detection using ML
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Machine Learning\Oasis Infobyte\Task 3/spam.csv")

data.info()

print(data.isnull().sum())

data.replace(to_replace = 'ham', value = 1, inplace = True)
data.replace(to_replace = 'spam', value = 0, inplace = True)

X = data.v2
Y = data.v1

sn.histplot(Y)
plt.show()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,train_size=0.9,random_state=25)

gok = pd.concat([x_train,y_train], axis = 1)

# Seperate spam in seperate variable
spam = gok[gok.v1 == 0]
ham = gok[gok.v1 == 1]