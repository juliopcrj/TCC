setwd("workspace/TCC/")

stats = read.csv("output.csv")

library(neuralnet)

data.norm = as.data.frame(sapply(stats, unclass))

scale_column = function(x){
  return (x-min(x))/(max(x)-min(x))
}

data.norm = as.data.frame(lapply(data.norm, scale_column))
amostra = 0.7 * nrow(data.norm)
index = sample(seq_len(nrow(data.norm)), size=amostra)

data.train = data.norm[index,]
data.test = data.norm[-index,]

'%!in%' <- function(x,y)!('%in%'(x,y)) #MAGIC!

nn <- neuralnet(p1_shoot + p1_horizontal + p1_vertical~p1_x + p1_y + p1_score + p2_x +
                  p2_y + p2_horizontal + p2_vertical + p2_shoot,
                data.train, hidden = 3)

prev = compute(nn, data.test[,-c(4, 5, 6)])


prev$net.result

nrow(prev$net.result)
nrow(data.test)
