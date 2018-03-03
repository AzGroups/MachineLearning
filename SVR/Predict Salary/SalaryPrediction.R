#Import dataset
source = read.csv('Position_Salaries.csv')

#Feature Scaling
#source = scale(source[,2:3])

#Creating a model
#install.packages('e1071')
library(e1071)
model = svm(formula = Salary ~ . ,data = source, type='eps-regression')

#Visualization
#install.packages('ggplot2')
library(ggplot2)
ggplot()+
  geom_point(aes(x = source$Level, y = source$Salary), colour='red') +
  geom_line(aes(x = source$Level, y = predict(model, newdata = source)), colour='green') +
  ggtitle('Salary Prediction') +
  xlab('Level') +
  ylab('Prediction')

#Visualization with high resolcution
#install.packages('ggplot2')
x_grid = seq(min(source$Level), max(source$Level), 0.1)
ggplot()+
  geom_point(aes(x = source$Level, y = source$Salary), colour='red') +
  geom_line(aes(x = x_grid, y = predict(model, newdata = data.frame(x_grid))), colour='green') +
  ggtitle('Salary Prediction') +
  xlab('Level') +
  ylab('Prediction')
  
