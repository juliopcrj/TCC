setwd("workspace/TCC/")

stats = read.csv("output.csv")

library(neuralnet)

data.norm = as.data.frame(sapply(stats, unclass))

scale_column = function(x){
  return (x-min(x))/(max(x)-min(x))
}

data.norm = as.data.frame(lapply(data.norm, scale_column))

names(data.norm)

'%!in%' <- function(x,y)!('%in%'(x,y))

nn <- neuralnet(p1_shoot + p1_horizontal + p1_vertical~p1_x + p1_y + p1_score + p2_x +
                  p2_y + p2_horizontal + p2_vertical + p2_shoot,
                data.norm, hidden = 3)


nrow(stats)
