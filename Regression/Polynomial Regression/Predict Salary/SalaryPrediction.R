#Import dataset
source = read.csv('Position_Salaries.csv')
source = source[,2:3]

#Split dataset -- Not required as the dataset is very small
#install.packages('caTools')
#library('caTools')
#split = sample.split(source$Salary, SplitRatio = 0.25)
#trainingSet = subset(source, split == FALSE)
#testSet = subset(source, split == TRUE)

#Feature scaling - Not required
#trainingSet[,1] = scale(trainingSet[,1])
#testSet[,1] = subset(testSet[,1])

#Creating a linear model
model = lm( formula = Salary ~ ., data = source )

#Creating a polynomial model
source$Level2 = source$Level^2
source$Level3 = source$Level^3
source$Level4 = source$Level^4
source$Level5 = source$Level^5
newModel = lm( formula = Salary ~ ., data = source )

#Visualization of Linear model 
#install.packages('ggplot2')
library('ggplot2')
ggplot() + 
  geom_point(aes(x = source$Level, y = source$Salary), colour = 'green') +
  geom_line(aes(x = source$Level, y = predict(model, newdata = source)),colour = 'blue') +
  ggtitle('Salary Prediction') + 
  xlab('Level') +
  ylab('Salary')

#Visualization of polynomial model 
#install.packages('ggplot2')
ggplot() + geom_point(aes(x = source$Level, y = source$Salary), colour = 'green') +
  geom_line(aes(x = source$Level, y = predict(newModel, newdata = source)),colour = 'blue') +
  ggtitle('Salary Prediction') + 
  xlab('Level') +
  ylab('Salary')

#Visualization of polynomial model with high resolution
#install.packages('ggplot2')
x_grid = seq(min(source$Level), max(source$Level), 0.1)
ggplot() + geom_point(aes(x = source$Level, y = source$Salary), colour = 'green') +
  geom_line(aes(x = x_grid, y = predict(newModel, newdata = data.frame(Level = x_grid,
                                                                    Level2 = x_grid^2,
                                                                    Level3 = x_grid^3,
                                                                    Level4 = x_grid^4,
                                                                    Level5 = x_grid^5))),
                                                                    colour = 'blue') +
  ggtitle('Salary Prediction') + 
  xlab('Level') +
  ylab('Salary')

#Prediction with Linear model
predict(model, data.frame(Level = 6.5))

#Prediction with polynomial model
predict(newModel, data.frame(Level = 6.5,
                             Level2 = 6.5^2,
                             Level3 = 6.5^3,
                             Level4 = 6.5^4,
                             Level5 = 6.5^5))

