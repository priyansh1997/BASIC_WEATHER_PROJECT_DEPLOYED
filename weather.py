import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import sklearn
def weather_pred(temp):
    df=pd.read_excel("Weather.xlsx")
    X=np.array(df.iloc[:,1:5])
    Y=np.array(df.iloc[:,5])
    Y=le().fit_transform(Y)
    lr=LinearRegression()
    mse=cross_val_score(lr,X,Y,cv=7,scoring='neg_mean_squared_error')
    #print(sorted(sklearn.metrics.SCORERS.keys()))
    lr.fit(X,Y)
    x_test=np.array(temp)
    x_test=x_test.reshape(1,-1)
    if lr.predict(x_test)>.5:
        today="Hot"
    else:
        today="Cold"
    return today

