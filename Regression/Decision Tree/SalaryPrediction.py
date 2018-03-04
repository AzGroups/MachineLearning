#Import libraries
import pandas as pan
import numpy as py
import matplotlib.pyplot as visuals

#Import dataset
source = pan.read_csv('Position_Salaries.csv')
x = source.iloc[:,1:2].values
y = source.iloc[:,2].values

#Feature Scaling - Not needed
'''from sklearn.preprocessing import StandardScaler
fScale = StandardScaler()
x = fScale.fit_transform(x)'''

#Creating a Model
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(x,y)

#Prediction
y_pred = model.predict(x)
y_predi = model.predict(6.5)
''' Model is not suitable for this dataset'''

#Visualization
visuals.scatter(x,y, color='aqua')
visuals.plot(x,y_pred, color='blue')
visuals.title('Salary prediction - Decision Tree')
visuals.xlabel('Job Level')
visuals.ylabel('Salary')
visuals.show()
'''Decision tree is non-linear so graph needs to non linear'''

#Visualization with high resolution
x_grid = py.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid),1))
visuals.scatter(x,y, color='aqua')
visuals.plot(x_grid,model.predict(x_grid), color='blue')
visuals.title('Salary prediction - Decision Tree')
visuals.xlabel('Job Level')
visuals.ylabel('Salary')
visuals.show()

#Not a right model

