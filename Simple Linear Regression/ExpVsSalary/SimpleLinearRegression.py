#Import Libraries
import numpy as num
import pandas as pan
import matplotlib.pyplot as visual

#Import Dataset
source = pan.read_csv('Salary_Data.csv')
x= source.iloc[:, :-1].values
y= source.iloc[:,1].values

#Update Missing Data
"""from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean', axis=0 )
imputer = imputer.fit(x[:, :-1])
x[:, :-1] = imputer.transform(x[:, :-1])"""

#Split Test/Train Data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)

#Feature Scaling -- Not needed for LR
## Single instance of the object can be fit once.
from sklearn.preprocessing import StandardScaler
fScale = StandardScaler()
x_train = fScale.fit_transform(x_train)
x_test = fScale.transform(x_test)

#Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

#Prediction
y_pred = model.predict(x_test)

#Visual Representation
visual.scatter(x_train, y_train, color= 'red')
visual.plot(x_train, model.predict(x_train), color='green')
visual.title('Salary Prediction based on Experience')
visual.xlabel('Experience')
visual.ylabel('Salary')
visual.show()