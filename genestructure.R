library(genemodel)

genemodel.plot(model=AT5G62640, start=25149433, bpstop=25152541, orientation="reverse", xaxis=T)

tabela <- read.csv("IntronExonTable.output", sep="\t", header=T)
tabela
AT5G62640

EI = strsplit(tabela$ExonIntronSeq[1], ",")
SE = strsplit(tabela$Starts.Ends[1], ",")
primeiro = data.frame(unlist(EI), unlist(SE))

colnames(primeiro) <- c("type", "coordinates")

for(i in 1:length(primeiro$type)){
	if(grepl("_", primeiro$type[i])){
		primeiro$type[i] = "intron"
	} else{
		primeiro$type[i] = "exon"
	}
}
primeiro
primeiro$coordinates[2]="14173923-14174099"
primeiro$coordinates[4]="14174270-14174461"
primeiro$coordinates[3]="14174100-14174572"
primeiro$coordinates[1]="14173749-14174572"
primeiro$coordinates[5]="14174462-14174572"
primeiro$coordinates[6]="14176406-14176542"
primeiro$coordinates[7]="14176612..14176691"
primeiro$coordinates[8]="14177175..14177477"
primeiro$coordinates[9]="2R:14177825..14178021"
primeiro$coordinates[10]="2R:14177840..14178021"
primeiro$coordinates[11]="2R:14177861..14178021"
primeiro$coordinates[12]="2R:14178098..14178200"
primeiro$coordinates[13]="2R:14178098..14178203"
primeiro$coordinates[14]=""
primeiro$coordinates[15]=""
primeiro$coordinates[16]=""
primeiro$coordinates[17]=""
primeiro$coordinates[18]=""
primeiro$coordinates[19]=""
primeiro$coordinates[20]=""


primeiro = primeiro[-c(2,3,4,5,10,11,12,13,18,19),]
genemodel.plot(model=primeiro, start=0, bpstop=3100, orientation="reverse", xaxis=T)

