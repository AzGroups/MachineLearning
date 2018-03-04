#Import libraries
import numpy as num
import pandas as pan
import matplotlib.pyplot as visuals

#Import dataset
source = pan.read_csv('50_Startups.csv')
x = source.iloc[:, :-1].values
y = source.iloc[:,4].values

#Encode data
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
encode_x = LabelEncoder()
x[:,3] = encode_x.fit_transform(x[:,3])
hotEncode = OneHotEncoder(categorical_features = [3])
x = hotEncode.fit_transform(x).toarray()

#Avoid Dummy varuable trap - Eliminate one dummy
x = x[:, 1:]

#Split data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train, y_test = train_test_split(x, y, test_size=0.25 )

#Feature Scaling
#Single instance can be fir once and transdorm ultiple times
from sklearn.preprocessing import StandardScaler
fScale = StandardScaler()
x_train = fScale.fit_transform(x_train)
x_test = fScale.transform(x_test)

#Creating a model - multi linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

#Prediction
y_pred = model.predict(x_test)

#Optimize - Backward elimination
import statsmodels.formula.api as optModel
x = num.append(arr = num.ones((50,1)).astype(int), values = x, axis =1 )
x_opt = x[:, [0,1,2,3,4,5]]
optimize = optModel.OLS(endog=y, exog = x_opt).fit()
optimize.summary()

#Eliminate - I
x_opt = x[:, [0,1,3,4,5]]
optimize = optModel.OLS(endog=y, exog = x_opt).fit()
optimize.summary()

#Eliminate - II
x_opt = x[:, [0,3,4,5]]
optimize = optModel.OLS(endog=y, exog = x_opt).fit()
optimize.summary()

#Eliminate - III
x_opt = x[:, [0,3,5]]
optimize = optModel.OLS(endog=y, exog = x_opt).fit()
optimize.summary()

#Eliminate - IV
x_opt = x[:, [0,3]]
optimize = optModel.OLS(endog=y, exog = x_opt).fit()
optimize.summary()

