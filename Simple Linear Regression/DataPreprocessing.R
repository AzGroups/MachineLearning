#Import Dataset
source = read.csv('Data.csv')

#Update Missing Data
source$Age = ifelse(is.na(source$Age),
                    ave(source$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                    source$Age)
source$Salary = ifelse( is.na(source$Salary),
                        ave(source$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        source$Salary)

#Encode Categorical Data
source$Country = factor(source$Country, 
                        levels = c('France', 'Spain', 'Germany'),
                        labels = c(0, 1, 2))
source$Purchased = factor(source$Purchased, 
                        levels = c('Yes', 'No'),
                        labels = c(1,0))

#Split Test/Train Data
#install.packages('caTools')
library(caTools)
split = sample.split( source$Purchased, SplitRatio= 0.75)
trainingSet = subset(source, split == TRUE)
testSet = subset(source, split == FALSE)

#Feature Scaling
trainingSet[, 2:3] = scale(trainingSet[, 2:3])
testSet[, 2:3] = scale(testSet[, 2:3])
