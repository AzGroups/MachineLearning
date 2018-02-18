#Import Dataset
source = read.csv('Salary_Data.csv')

#Split Train/Test data
#install.packages('caTools')
#library('caTools')
split = sample.split(source$Salary, SplitRatio = 0.75)
trainingSet = subset(source, split == TRUE)
testSet = subset(source, split == FALSE)

#Feature Scaling
trainingSet[,1] = scale(trainingSet[,1] )
testSet[,1] = scale(testSet[,1] )

#Linear Regression
model = lm(formula = Salary ~ YearsExperience, data = trainingSet )

#Prediction
prediction = predict(model, newdata = testSet)

#Visualization
#install.packages('ggplot2')
library('ggplot2')
ggplot()+ 
  geom_point( aes(x= trainingSet$YearsExperience, y = trainingSet$Salary), colour ='red') +
  geom_line(aes(x=trainingSet$YearsExperience,y=predict(model, newdata = trainingSet)), colour = 'green') +
  ggtitle('Salary estimation based on experience')+
  xlab('Experience')+
  ylab('Salary')


