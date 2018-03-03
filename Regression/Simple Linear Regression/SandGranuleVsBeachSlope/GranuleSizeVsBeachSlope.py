#Import Libraries
import numpy as num
import matplotlib.pyplot as visuals
import pandas as pan

#Import Dataset
source = pan.read_csv('Sand_Data.csv')
x = source.iloc[:,:-1 ].values
y = source.iloc[:, 1].values

#Split Dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size= .20, random_state = 275427)

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

visuals.scatter(x_train, y_train, color='blue')
visuals.plot(x_train, model.predict(x_train), color = 'green')
visuals.title('Sand granule size Vs Beach slope')
visuals.xlabel('Diameter of Sand granule')
visuals.ylabel('Beach slope')
visuals.show()