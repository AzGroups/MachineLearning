#Import libraries
import numpy as num
import pandas as pan
import matplotlib.pyplot as visuals

#Import dataset
source = pan.read_csv('Position_Salaries.csv')
x = source.iloc[:,1:2].values
y = source.iloc[:, 2].values

#No Split because the dataset is small
''''from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)'''

#Creating a linear model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)

#Visualization
visuals.scatter(x,y, color = 'green')
visuals.plot(x,model.predict(x), color='blue')
visuals.title('Predicting salary')
visuals.xlabel('Position')
visuals.ylabel('Salary')
visuals.show()

#Creating polynomial Model - Linear is unfit
from sklearn.preprocessing import PolynomialFeatures
updateData = PolynomialFeatures(degree=5)
poly_x = updateData.fit_transform(x)
updateData.fit(poly_x,y)

newModel = LinearRegression()
newModel.fit(poly_x,y)

#Visualization
visuals.scatter(x,y,color='red')
visuals.plot(x, newModel.predict(updateData.fit_transform(x)), color='blue')
visuals.title('Predicting salary')
visuals.xlabel('Position')
visuals.ylabel('Salary')
visuals.show()

#Visualization with highter resolution
x_grid = num.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
visuals.scatter(x,y,color='red')
visuals.plot(x_grid, newModel.predict(updateData.fit_transform(x_grid)), color='blue')
visuals.title('Predicting salary')
visuals.xlabel('Position')
visuals.ylabel('Salary')
visuals.show()

#Prediction
model.predict(6.5)
newModel.predict(updateData.fit_transform(6.5))
