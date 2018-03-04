#import dataset
source = read.csv('Position_Salaries.csv')
source = source[2:3]

#Create a model
#install.packages('randomForest')
set.seed(4)
library('randomForest')
model = randomForest(x = source[1],
                     y=source$Salary,
                     ntree =40)

#Prediction
#y_pred = predict(model, newdata = source)

_
#Predict data for somone with level inbetween 6-7
Y_pred1 = predict(model, data.frame(Level = 6.5))

#Visualization - Linear
#install.packages('ggplot2')
#library(ggplot2)
ggplot() +
  geom_point(aes(x= source$Level, y = source$Salary), colour ='red') +
  geom_line(aes(x = source$Level, y = predict(model, newdata = source, colour = 'green'))) +
  ggtitle('Salary prediction with Random Forest') +
  xlab('Level') +
  ylab('Salary')


#Visualization - Non linear - Higher resolution
#install.packages('ggplot2')
#library(ggplot2)
x_grid = seq(min(source$Level), max(source$Level), 0.1)
#Incr. resolution from 0.1 to 0.01/0.001 to make the seperations more vertical
x_grid = seq(min(source$Level), max(source$Level), 0.001)
ggplot() +
  geom_point(aes(x= source$Level, y = source$Salary), colour ='red') +
  geom_line(aes(x = x_grid, y = predict(model, newdata = data.frame(Level=x_grid), colour = 'green'))) +
  ggtitle('Salary prediction with Random Forest') +
  xlab('Level') +
  ylab('Salary')
