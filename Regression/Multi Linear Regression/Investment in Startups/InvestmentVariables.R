#Import dataset
source = read.csv('50_Startups.csv')

#Encode data
source$State = factor(source$State, levels = c('New York', 'California', 'Florida'),
                      labels = c(0,1,2))

#Split dataset
#install.packages('caTools')
library(caTools)
split = sample.split(source$Profit, SplitRatio = 0.75)
trainigSet = subset(source, split == TRUE)
testSet = subset(source, split == FALSE)

#Scaling the dataset
trainigSet[,1:3] = scale(trainigSet[,1:3])
testSet[,1:3] = scale(testSet[,1:3])

#Creating a model
model = lm(formula = Profit ~ ., data = source)
summary(model)

#Prediction
y_prediction = predict(model, newdata = testSet)

#Backward Elimination
model = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend +State, 
           data = source)
summary(model)

model = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, 
           data = source)
summary(model)

model = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, 
           data = source)
summary(model)

model = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, 
           data = source)
summary(model)