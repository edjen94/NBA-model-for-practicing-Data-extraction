# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:16:32 2022

@author: jvsla
"""

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import mutual_info_regression
df1=pd.read_csv('2012-13_merged.csv')


X=df1.copy().dropna()
y=X.pop('Homewin')

model=RandomForestClassifier()
model.fit(X,y)

num_features=10
features=X.columns
importances=model.feature_importances_
indices = np.argsort(importances)

#plt.figure(figsize=(10,100))
plt.title('Feature Importances')
plt.barh(range(num_features), importances[indices[-num_features:]], color='b', align='center')
plt.yticks(range(num_features), [features[i] for i in indices[-num_features:]])
plt.xlabel('Relative Importance')
plt.show()


'''
(pd.Series(model.feature_importances_, index=X.columns)
#   .nlargest(20)
   .plot(kind='barh'))   
'''


    
    