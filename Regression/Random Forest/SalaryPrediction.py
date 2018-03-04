#Import Libraries
import numpy as nm
import pandas as p
import matplotlib.pyplot as visuals

#Import dataset
source = p.read_csv('Position_Salaries.csv')
x = source.iloc[:,1:2].values
y = source.iloc[:,2].values

#Create a model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 500)
model.fit(x,y)

#Predict
#y_pred = model.predict(x)

#Predict salary for someone on 6.5
y_pred1 = model.predict(6.5)

#Visualization -- very linear
visuals.scatter(x,y, color='red')
visuals.plot(x,model.predict(x), color='green')
visuals.title('Salary Estimation by Random Forest')
visuals.xlabel('Level')
visuals.ylabel('Salary')
visuals.show()

#Visualization - High defination 
x_grid = nm.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid),1))
visuals.scatter(x,y, color='red')
visuals.plot(x_grid,model.predict(x_grid), color='green')
visuals.title('Salary Estimation by Random Forest')
visuals.xlabel('Level')
visuals.ylabel('Salary')
visuals.show()