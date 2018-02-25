#Import Dataset
source = read.csv('Auto-Insurance.csv')

#Split data
#install.packages('caTools')
library('caTools')
split = sample.split(source$Total.cost.in.Swedish.Kronor..thousnads., SplitRatio = 0.23)
trainingSet = subset(source, split == FALSE )
testSet = subset(source, split == TRUE )

#Feature Scaling
trainingSet[,1] = scale(trainingSet[,1])
testSet[,1] = scale(testSet[,1])

#Linear Regression=
model = lm(formula = Total.cost.in.Swedish.Kronor..thousnads. ~ No..of.Claims, data = trainingSet )

#Prediction
prediction = predict(model, newdata = testSet)

#Visualizartion
#install.packages('ggplot2')
library('ggplot2')
ggplot()+
  geom_point(aes(x=trainingSet$No..of.Claims, y = trainingSet$Total.cost.in.Swedish.Kronor..thousnads.), colour ='blue') +
  geom_line(aes(x=trainingSet$No..of.Claims, predict(model, newdata = trainingSet)), colour='green')+
  ggtitle('Sand granule based on beach slope')+
  xlab('Granule size')+
  ylab('Beach slope')



