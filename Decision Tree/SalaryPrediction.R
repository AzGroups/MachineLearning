#Import dataset
source = read.csv('Position_Salaries.csv')
source = source[,2:3]

#Create the model
#install.packages('rpart')
library('rpart')
model = rpart(formula = Salary ~ .,
              data = source,
              control = rpart.control(minsplit=1))
y_pred = predict(model, newdata = source)

#Predict for someone  at 6.5
y_pred1 = predict(model, data.frame(Level = 6.5))
## Not accurate - Not a suitable model 

#Visualization
ggplot()+
  geom_point(aes(x = source$Level, y = source$Salary), colour = 'red') +
  geom_line(aes(x=source$Level, y = predict(model, newdata = source)), colour ='green') +
  ggtitle('Salary Prediction by Decision Tree')+
  xlab('Level')+
  ylab('Salary')