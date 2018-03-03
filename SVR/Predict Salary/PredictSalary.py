#Import Libraries
import numpy as num
import pandas as pan
import matplotlib.pyplot as visuals

#Import dataset
source = pan.read_csv('Position_Salaries.csv')
x = source.iloc[:,1:2].values
y = source.iloc[:, 2:3].values
#Split data -- Dataset is small so no need to split the data

#Feature scaling
from sklearn.preprocessing import StandardScaler
#fScale = StandardScaler()
#fScale_x = fScale.fit_transform(x)
fScaled_x = StandardScaler()
fScaled_y = StandardScaler()
x = fScaled_x.fit_transform(x)
y = fScaled_y.fit_transform(y)

#Creating a model
from sklearn.svm import SVR
model = SVR()
model.fit(x,y)

#Visualizattion
visuals.scatter(x,y, color ='red')
visuals.plot(x,model.predict(x), color = 'aqua')
visuals.title('Salary Prediction')
visuals.xlabel('Level')
visuals.ylabel('Salary')
visuals.show()

#Prediction
prediction = fScaled_y.inverse_transform(model.predict(fScaled_x.transform(num.array([[6.5]]))))