library(stringr)
library(Biostrings)

source("nfs/scistore03/vicosgrp/jraices/programs/functions1.R")

library(genemodel)

genemodel.plot(model=AT5G62640, start=25149433, bpstop=25152541, orientation="reverse", xaxis=T)

spl1<-data.frame(
  type=c("5' utr", "coding_region", "intron", "coding_region", "intron", "coding_region","3' utr"), 
    coordinates=c("1-50", "50-100", "100-150", "150-200", "200-250", "250-300","300-350"))

spl2<-data.frame(type=c("coding_region", "coding_region", "coding_region","coding_region","coding_region", "coding_region","3' utr"), coordinates=c("1-50", "50-95", "100-250", "250-300","300-350","400-2000", "2441-2442"))
par(mfrow=c(2,1))
genemodel.plot(model=spl1, start=1, bpstop=2442, orientation="reverse", xaxis=T)
genemodel.plot(model=spl2, start=1, bpstop=2442, orientation="reverse", xaxis=F)

tablMaker <- data.frame(type=c("coding_region","coding_region","coding_region","coding_region","coding_region","coding_region","intron", "3' utr"), coordinates=c("717-878","880-1047","1047-1278","1278-1445","1445-1578","1578-1825","1825-2411","2441-2442"))
genemodel.plot(model=tablMaker, start=1, bpstop=2442, orientation="reverse", xaxis=T)#, title="m54067_190619_133211_13500933_ccs")
mine <- data.frame(type<-c("coding_region","coding_region","coding_region","coding_region","coding_region","coding_region","intron","3' utr"), coordinates<-c("717-878","880-1047","1047-1278","1278-1445","1445-1578","1578-1825","1825-2411","2441-2442"))
genemodel.plot(model=mine, start=1, bpstop=2442, orientation="reverse", xaxis=F)

