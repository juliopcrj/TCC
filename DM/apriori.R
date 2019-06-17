require("arules")
setwd("/home/jio/workspace/TCC/DM/")
dataset = read.csv("output.csv")

# Seleção
data_names = names(dataset)
selected_names = data_names[c(1, 2, 4, 6, 7, 8, 9, 11, 14)]
clean_dataset = subset(
  dataset,
  select = selected_names
)

# Transformação
clean_dataset$p1_horizontal = sapply(clean_dataset$p1_horizontal, unclass)
clean_dataset$p2_horizontal = sapply(clean_dataset$p2_horizontal, unclass)
# Transformação PT.2
cd_size = nrow(clean_dataset)
cd_frames = c()

# Pra facilitar os cálculos, estou usando apenas cada quarto elemento
# O que significa um frame por segundo a ser processado
for(i in 1:cd_size){
  if((i-1)%%4 == 0){
    cd_frames = c(cd_frames, i)
  }
}
shrinked_dataset = clean_dataset[cd_frames,]

# Pré-processamento

sd_size = nrow(shrinked_dataset)
for (i in sd_size:2){
  shrinked_dataset$p1_score[i] = as.integer( shrinked_dataset$p1_score[i] > shrinked_dataset$p1_score[i-1])
  shrinked_dataset$p2_score[i] = as.integer( shrinked_dataset$p2_score[i] > shrinked_dataset$p2_score[i-1])
}

shrinked_dataset$p1_y = as.integer(shrinked_dataset$p1_y)
