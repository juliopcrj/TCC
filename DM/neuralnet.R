setwd("..")

stats = read.csv("output.csv")

library(neuralnet)

data.norm = as.data.frame(sapply(stats, unclass))

scale_column = function(x){
  return (x-min(x))/(max(x)-min(x))
}

data.norm = as.data.frame(lapply(data.norm, scale_column))
