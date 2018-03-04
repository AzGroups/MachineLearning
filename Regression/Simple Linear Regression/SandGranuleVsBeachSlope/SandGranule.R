#Import Dataset
source = read.csv('Sand_Data.csv')

#Split data
#install.packages('caTools')
library('caTools')
split = sample.split(source$Slope.of.Beach, SplitRatio = 0.23)
trainingSet = subset(source, split == FALSE )
testSet = subset(source, split == TRUE )

#Feature Scaling
trainingSet[,1] = scale(trainingSet[,1])
testSet[,1] = scale(testSet[,1])

#Linear Regression=
model = lm(formula = Slope.of.Beach ~ Diameter, data = trainingSet )

#Prediction
prediction = predict(model, newdata = testSet)

#Visualizartion
#install.packages('ggplot2')
library('ggplot2')
ggplot()+
  geom_point(aes(x=trainingSet$Diameter, y = trainingSet$Slope.of.Beach), colour ='blue') +
  geom_line(aes(x=trainingSet$Diameter, predict(model, newdata = trainingSet)), colour='green')+
  ggtitle('Sand granule based on beach slope')+
  xlab('Granule size')+
  ylab('Beach slope')



