#Import libraries
import pandas as p
import numpy as n
import matplotlib.pyplot as visuals

#Import libraries
source = p.read_csv('Social_Network_Ads.csv')
x= source.iloc[:,2:4].values
y= source.iloc[:,4].values

#Splitting the data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
fScale = StandardScaler()
x_train = fScale.fit_transform(x_train)
x_test = fScale.transform(x_test)

#Creating a model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)

#Prediction
y_pred = model.predict(x_test)

#Confusion matrix
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test,y_pred)

#Visualization
from matplotlib.colors import ListedColormap
x_set,y_set = x_train, y_train
x1,x2 = n.meshgrid(n.arange(start = x_set[:,0].min() -1, stop = x_set[:,0].max()+1, step = 0.001),
                    n.arange(start = x_set[:,1].min() -1, stop = x_set[:,1].max()+1, step = 0.001))
visuals.contourf(x1,x2, model.predict(n.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
                 alpha = 0.75, cmap = ListedColormap(('red','green')))
visuals.xlim(x1.min(), x1.max())
visuals.ylim(x2.min(), x2.max())
for i,j in enumerate(n.unique(y_set)):
    visuals.scatter(x_set[y_set ==j, 0], x_set[y_set ==j,1],
    c= ListedColormap(('red','green'))(i), label = j)
visuals.title('Predict uers who buy certain item - Logistic Regression')
visuals.xlabel('Age')
visuals.ylabel('Salary')
visuals.legend()
visuals.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = n.meshgrid(n.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
                     n.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
visuals.contourf(x1, x2, model.predict(n.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
visuals.xlim(x1.min(), x1.max())
visuals.ylim(x2.min(), x2.max())
for i, j in enumerate(n.unique(y_set)):
    visuals.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
visuals.title('Predict uers who buy certain item - Logistic Regression')
visuals.xlabel('Age')
visuals.ylabel('Salary')
visuals.legend()
visuals.show()