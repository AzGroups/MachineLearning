#Import Libraries
import numpy as num
import matplotlib.pyplot as visuals
import pandas as pan

#Import Dataset
source = pan.read_excel('Auto Insurance.xlsx')
x = source.iloc[:,:-1 ].values
y = source.iloc[:, 1].values

#Split Dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size= .25, random_state = 275427)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
fScale = StandardScaler()
x_train = fScale.fit_transform(x_train)
x_test = fScale.transform(x_test)

#Creating a model - Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

#Prediction
y_pred = model.predict(x_test)

#Visualization

visuals.scatter(x_train, y_train, color='aqua')
visuals.plot(x_train, model.predict(x_train), color = 'blue')
visuals.title('Claims Vs Total Cost in Swedish Kronor (thousnads)')
visuals.xlabel('Total claims')
visuals.ylabel('Total Cost in Swedish Kronor (thousnads)')
visuals.show()