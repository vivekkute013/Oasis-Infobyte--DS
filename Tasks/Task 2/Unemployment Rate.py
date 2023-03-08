# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:25:27 2023

@author: Vivek
"""

# Unemployeement Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("D:\Machine Learning\Oasis Infobyte\Task 2/Unemployment in India.csv")

#missing = data.isnull().sum()

data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Area"]

plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Area", data=data)
plt.show()

plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Area", data=data)
plt.show()

# unemployment = data[['States', 'Area', 'Estimated Unemployment Rate']]

