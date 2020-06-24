library(genemodel)

genemodel.plot(model=AT5G62640, start=25149433, bpstop=25152541, orientation="reverse", xaxis=T)

tabela <- read.csv("IntronExonTable.output", sep="\t", header=T)

primeiro = data.frame(unlist(strsplit(tabela$ExonIntronSeq[1], ",")), unlist(strsplit(tabela$Starts.Ends[1], ",")))
