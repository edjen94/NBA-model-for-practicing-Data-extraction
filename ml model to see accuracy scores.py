# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 07:23:36 2022

@author: jvsla
"""

import pandas as pd 
from sklearn.model_selection import train_test_split
df1=pd.read_csv('2012-13_merged.csv')
X=df1.copy().dropna()
y=X.pop('Homewin')
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)


'''
#svc model
from sklearn.svm import LinearSVC
lclf=LinearSVC(random_state=0, tol=1e-5, max_iter=1000)
lclf.fit(X_train, y_train)
print(lclf.score(X_test,y_test))
#63%accuracy - average of running 5 times
'''
'''
#knn model
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
#60.8%-- average of running 5 times
'''
'''
from sklearn.svm import SVC
from sklearn import svm
clf = SVC(gamma='scale',probability=True)
clf.fit(X_train, y_train)
print(clf.score(X_test,y_test))
#61% accuracy- average of running 5 times
'''
'''
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
advclf = BaggingClassifier(base_estimator=SVC(gamma='scale'), n_estimators=10, random_state=0)
advclf.fit(X_train, y_train)
advclf.score(X_test,y_test)

# Random Forest Classification model (Accuracy of 72.17%)
from sklearn.ensemble import RandomForestClassifier
rdf = RandomForestClassifier(max_depth=8, random_state=0, n_estimators=300)
rdf.fit(X_train, y_train)
rdf.score(X_test,y_test)

# XGBoost Classification (Accuracy of 68.61%)
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
xgbModel = XGBClassifier()
xgbModel.fit(X_train, y_train)
xgbPredictions = xgbModel.predict(X_test)
xgbAccuracy = accuracy_score(y_test, xgbPredictions)
'''


