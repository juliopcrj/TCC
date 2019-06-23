setwd("/home/jio/workspace/TCC/DM/")
raw_data <- read.csv("output.csv")
sel_colums <- c("p1_x", "p1_y", "p1_score", "p2_x", "p2_y")
sel_data <- raw_data[,sel_colums]

si = nrow(sel_data)

for ( i in si:2){
  if(sel_data$p1_score[i] > sel_data$p1_score[i-1]){
    sel_data$p1_score[i] <- 1
  }else{
    sel_data$p1_score[i] <- 0
  }
}


# Gambiarra! Seta os 3 valores anteriores a um acerto para 1
# isto é para aceitar as posições do personagem enquanto o 
# projétil ainda está a caminho
for ( i in 1:si){
  if( sel_data$p1_score[i] == 1){
    sel_data$p1_score[i-3] <- 1
    sel_data$p1_score[i-2] <- 1
    sel_data$p1_score[i-1] <- 1
  }
}

# Selecionando apenas as linhas onde houve pontuação
was_score = sel_data[,"p1_score"] ==1
sel_data = sel_data[was_score,]

sel_data <- data.frame(sapply(sel_data, as.factor))

require("arules")
rules = apriori(sel_data, parameter = list(conf=0.1, supp=0.2, target="rules"))



