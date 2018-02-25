#Import libraries
import numpy as num
import matplotlib.pyplot as plot
import pandas as pan

#Import Dataset
source = pan.read_csv('Data.csv')
x = source.iloc[:, :-1].values
y = source.iloc[:, 3].values

#Update Missing Data

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

#Encode Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encode_x = LabelEncoder()
x[: ,0] = encode_x.fit_transform(x[: ,0])
hotEncodeRow1 = OneHotEncoder(categorical_features=[0])
x = hotEncodeRow1.fit_transform(x).toarray()
encodeY= LabelEncoder()
y=encodeY.fit_transform(y)

#Split Test/Train Data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)

#Feature Scaling
## Single instance of the object can be fit once.
from sklearn.preprocessing import StandardScaler
fScale = StandardScaler()
x_train = fScale.fit_transform(x_train)
x_test = fScale.transform(x_test)