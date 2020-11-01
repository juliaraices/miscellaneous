library(genemodel)

genemodel.plot(model=AT5G62640, start=25149433, bpstop=25152541, orientation="reverse", xaxis=T)

tabela <- read.csv("~/dmel_analysis/gonads/raws/tempF1.txt", sep="\t", header=T)
head(tabela)
head(AT5G62640)

EI = strsplit(tabela$ExonIntronSeq[1], ",")
SE = strsplit(tabela$Starts.Ends[1], ",")
primeiro = data.frame(unlist(EI), unlist(SE))

colnames(primeiro) <- c("factor", "ranges")

for(i in 1:length(primeiro$type)){
	if(grepl("co", primeiro$type[i])){
		primeiro$type[i] = "exon"
	} else{
		primeiro$type[i] = "intron"
	}
}

GRanges(primeiro)
primeiro[7,1] = "coding_region"
primeiro[7,2] = "7076710-7092667"
primeiro[5,1] = "exon"
primeiro[6,1] = "intron"
primeiro[6,2] = "7082026-7084598"
genemodel.plot(model=primeiro, start=7066700, bpstop=7100000, orientation="reverse", xaxis=T)

library(ggbio)
library(biovizBase)

ggplot() + geom_alignment(primeiro, type = "model")
autoplot(primeiro, aes(type = model))

library(GenomicRanges)
grfr <- GRanges(seqnames = sample(c("chr1", "chr2", "chr3"), size = N, replace = TRUE), IRanges(start = sample(1:300, size = N, replace = TRUE), width = sample(70:75, size = N,replace = TRUE)), strand = sample(c("+", "-"), size = N, replace = TRUE), value = rnorm(N, 10, 3), score = rnorm(N, 100, 30), sample = sample(c("Normal", "Tumor"), size = N, replace = TRUE), pair = sample(letters, size = N, replace = TRUE))
auplot(primeiro, aes(color = strand, fill = strand))

autoplot(object, ..., xlab, ylab, main, which)
autoplot(object, ..., xlab, ylab, main,
        geom = c("tile", "raster"), axis.text.angle = NULL,
        hjust = 0.5, na.value = NULL,
        rownames.label = TRUE, colnames.label = TRUE,
        axis.text.x = TRUE, axis.text.y = TRUE)


source("https://bioconductor.org/biocLite.R") 
biocLite("Gviz")


plot.new()
axis(1, seq(0, 1, 0.2))

GeneStructure <- function(x){
	for(i in 1:length(x)){
		x$rang[i] <- strsplit(x$Starts.Ends[i], ",")[[1]]
		for(j in 1:length(x$rang[i])){
			XX[j] <- strsplit(x$rang[i][j], "-")[[1]]
			a = 0.5 + i
			b = 0.5 + i*2
			ggplot(XX, aes(XX[1],XX[2],a,b,"cornflowerblue")) + geom_rect()
		}
	}
}

ggplot() + geom_rect(tabela, aes)
tabela$cores <- "cornflowerblue"
tabela
GeneStructure(tabela)
primeiro

library(plotly)

library(data.table)
df<-data.table(Product=letters[1:10], minX=1:10, maxX=5:14, minY= 10:1, maxY=14:5)
NewTable <- data.frame(Read=character(), XX1=integer(), XX2=integer(), YY1=integer(), YY2=integer())
for(i in length(tabela)){
	partOne <- strsplit(tabela$Starts.Ends[i], ",")[[1]]
	for(j in length(partOne)){
		partThree <- strsplit(partOne[j], "-")
		NewTable$Read[nrow(NewTable)+1] <- tabela$transcript[i]
		NewTable$XX1[nrow(NewTable)+1] <- partThree[[1]][1]
		NewTable$XX2[nrow(NewTable)+1] <- partThree[[1]][2]
		NewTable$YY1[nrow(NewTable)+1] <- c(0.5+i)
		NewTable$YY2[nrow(NewTable)+1] <- c(0.5+2*i)
	}
}
a <- strsplit(partOne[1], "-")[[1]]
a
partOne[2]
partThree
NewTable
df.t<-data.table(rbind( df[,list(Product,X=minX,Y=minY)],
        df[,list(Product,X=minX,Y=maxY)],
        df[,list(Product,X=maxX,Y=minY)],
        df[,list(Product,X=maxX,Y=maxY)]))[order(Product,X,Y)]
p <- ggplot(df,aes(xmin=minX,xmax=maxX,ymin=minY,ymax=maxY,fill=Product))+ geom_rect()
fig <- ggplotly(p)
fig



plot.new() 
axis(2, seq(7076710, 7092667, 1000))
ggplot(aes()) + geom_rect(aes(x=c(10,325,10,325), y=c(1,1,1.5,1.5), fill="cornflowerblue"))

grid(led = 2)


plot(runif(10), runif(10), 
          xlim=c(0, 1), ylim=c(0,1), 
	       axes=FALSE, #Don't plot the axis 
	       type="n",  #hide the points
	            ylab="", xlab="") #No axis labels""""""')))))

