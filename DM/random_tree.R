library(randomForest)
library(dplyr)

getwd()
setwd("C:/Users/julio/workspace/TCC/")

data = read.csv("output.csv")


targets = cbind(data$p1_horizontal, data$p1_vertical, data$p1_shoot)
targets = targets[,1]*100 + targets[,2]*10 + targets[,3]
targets

values = c("p1_horizontal", "p1_vertical", "p1_shoot")

'%!in%' <- function(x,y)!('%in%'(x,y)) #MAGIC!

data = cbind(select(data, c(-p1_shoot, -p1_horizontal, -p1_vertical)), targets)

data

set.seed(100)

amostra = sample(nrow(data), 0.7*nrow(data), replace = F)
train_set = data[amostra,]
test_set = data[-amostra,]

RF = randomForest(formula = targets ~ ., data = train_set, importance = T)

RF

pred_train = predict(RF, train_set, type = "class")
table(pred_train, train_set$targets)
# Terrible.

