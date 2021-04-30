#Julia Raices
#March 2020
#Let's get our functions together!!! \o/

qualiPACBio <- function(x){ #give file opened with readDNAStringSet
# this is a small function, that I am now trying to make into a function, here is what is does
	endAs <- numeric() 
	midAs <- numeric()
	begTs <- numeric()
	midTs <- numeric()
	for(l in 1:length(x)){
		half = ceiling(width(x[l])/2)
		if(width(x[l])<=100){
			endAs <- append(endAs,(str_count(subseq(x[[l]],start=(-half), end=-1), "A")/half)) # check how many As in the last bps
			begTs <- append(begTs,(str_count(subseq(x[[l]],start=1, end=half), "T")/half)) # and how many Ts at the first bps
			# and add those values to their respective arrays
			midAs <- append(midAs, NA) # check how many As in the middle 100 bps
			midTs <- append(midTs, NA) # and how many Ts at the middle 100 bps
		}else{
			endAs <- append(endAs,(str_count(subseq(x[[l]],start=-100, end=-1), "A")/100)) # check how many As in the last bps
			begTs <- append(begTs,(str_count(subseq(x[[l]],start=1, end=100), "T")/100)) # and how many Ts at the first bps
			# and add those values to their respective arrays
			midAs <- append(midAs,(str_count(subseq(x[[l]], start=(half-50), end=(half+49)), "A")/100)) # check how many As in the middle 100 bps
			midTs <- append(midTs,(str_count(subseq(x[[l]], start=(half-50), end=(half+49)), "T")/100)) # and how many Ts at the middle 100 bps
		}
	}
        return(list(endAs=endAs,begTs=begTs,midAs=midAs,midTs=midTs))	# returns all the arrays you want
}

counts_fpkm <- function(y, exp, column){
	PC_reads = data.frame(geneFB=character(), geneCG=character(), reads=integer(), fpkm=numeric())
	# creates two new table, where we store the amount of reads for each gene and the amount of reads and fpkm
	eita <- as.data.frame(t(table(y[,14])))
	for(l in 1:length(eita[,2])){ # for each pair gene/reads
		# get FPKM expression from expression table
		# get it for 5 day old flies (because that's how old our flies were)
		fspkms=numeric()
		CG=character()
		fspkms=exp[eita[l,2] %in% exp[2], column]
		CG=exp[eita[l,3] %in% exp[2], 1]
		if(length(fspkms)==0){
			fspkms=NA
		}
		if(length(CG)==0){
			CG=NA
		}
		temp=data.frame(geneFB=eita[l,2], geneCG=CG, reads=eita[l,3], fpkm=fspkms)
		PC_reads <- rbind(PC_reads, temp) # actrually add the reads to the read dataframe
	}
	# this two dataframes is to be able to do plots easily with it all
	return(PC_reads)
}


### Updated March 2021

myToPlot <- function(tabela){
	# This function creates an array of datyaframes with the coordinates so we can plot them with genemodel.plot, from the librare genemodel
	# the "tabela" input corresponds to the output of my own code to make an exon/intron table (i.e table_creator.py).
	# The header of such table is (or is very similar to, mantaining the general order of):
	# [1]Transcript [2]Gene [3]Exon/Intron.Sequence [4]TranscriptSize [5]Starts-EndsOfExon/IntronMatchesInTranscript [6]UniqueIDs [7]Flags [8]Sequence
	# We still need to find a way to change the coordinate to chrmosome coordinates
	Plotable = list()
	#creates a new dataframe to store the altered reads/trascripts so we can use it with "genemodel" library
	for(l in 1:nrow(tabela)){ #for each row
		readName = tabela$Transcript[l]
		geneFB = tabela$Gene[l]
		numero = l
		bpstop = 2000
		temp1 <- (strsplit(tabela$Starts.Ends[l], ","))
		temp3 <- rep("coding_sequence", length(temp1))
		temp2  <- data.frame(type=temp3, coordinates=temp1)
		Plotable[[l]] <- temp2
		names(Plotable[[l]]) <- c("type", "coordinates")
	}
	return(Plotable)
}












