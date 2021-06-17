#!bin/usr/python3
## import packages we will need to work with dataframes and all
import sys, argparse, os, csv # import packages to call commands, to parse arguments given when calling the program
from Bio import SeqIO # import part of the Bio package that deals with input and output of sequences/fasta/fastq/etc
import pandas as pd # pandas is for dealing with dataframes
pd.options.mode.chained_assignment = None # default='warn' # changes the options for pandas so it doesn't give warmings for everything. in other words: I'm bad and I don't want to know about it =/
from datetime import datetime # allows us to add the date/time to the code/output

# read inputs:
# allows to create an automatic message for usage and checks if all the parameters have been provided, or give the default input for each parameter that has a default value/file
parser = argparse.ArgumentParser(description='Program to create a table with the list of introns/exons that comprise different reads.') # sets the description for the full program, in case it's called with no arguments
parser.add_argument("--blat", required=True, type=str, help='Output from blat of reads against introns and exons.') # states a required argument, a blat file, and has a helper message in case you don't provide it, or ask for help
#inputz = pd.read_table("~/AS/dmel_analysis/gonads/raws/F1Gonads_ExonIntron.final.blat", header=None, sep='\t')#, escapechar='\\')# read input into a dataframe # for debugging purposes
parser.add_argument("--alldoer", default="/nfs/scistore03/vicosgrp/jraices/programs/AllThings.output", type=str, help='Blat output from intron+exons used for your reads, but this time, against a full gene/extended gene dataset. Default is the blat output for extended genes vs exons+introns in Drosophila melanogaster') # sets the default genome blat file to be used in case it is not provided by the user
#alldoer = pd.read_table("/nfs/scistore03/vicosgrp/jraices/programs/AllThings.output", sep='\t', na_values="NA", )#, escapechar='\\')# read input into a dataframe # for debugging purposes
parser.add_argument("--fastQuery", required=True, type=str, help='Reads/data used in blat against introns and exons') # states a required argument, a fasta file, and has a helper message in case you don't provide it, or ask for help
#fastaQuery = open("/nfs/scistore03/vicosgrp/jraices/AS/dmel_analysis/gonads/raws/F1Gonads.fasta", "r") # opens file as read only #for debugging purposes
parser.add_argument("--output", default="IntronExonTable.output", help="Desired name for the output file. Default is IntronExonTable.output", type=str) # sets the output file name if none is given. If there's already a file with that name, it will be overwritten.
#outputz = open("IntronExonTable.output", "w") # "w" will overwrite file #for debugging purposes
parser.add_argument("--log", default="TableMaker.log", help="Desired name for the log file. Default is TableMaker.log", type=str) # sets the log file name if none is given. The new log will be appended to the end of the given file.
#log = open("TableMaker.log", "a") # "a" will append to the end of the file # for debugging purposes

args = parser.parse_args()

# checkif all files open
try: # makes sure you can open all the files
    log = open(args.log, "a") # "a" will append to the end of the file
    # open input
    inputz = pd.read_table(args.blat, header=None, sep='\t')#, escapechar='\\')# read input into a dataframe
    alldoer = pd.read_csv(args.alldoer, sep='\t', na_values="NA")#, converters={"CorrectedExonIntronLociInChromosome":str})#, escapechar='\\')# read input into a dataframe
    fastaQuery = open(args.fastQuery, "r") # opens file as read only
    outputz = open(args.output, "w") # "w" will overwrite file
#if files do not open:
except FileNotFoundError or IOError: # if any of the files is not openned, shuts down the program and logs the errors
    # report to log
    log.write("One or more of the files given was not available.\n") # prints error to log
    print("File name is not valid. Please try again.") # prints error to standard output
    # exit program with erros
    sys.exit("Files are not valid.") # prints error as system error and leaves the program


#write the used files and when it was started
log.write("\n\n#########################\nNew usage of table_creator.py at " + str(datetime.now()) + ".\n\t The input used was " + str(args.blat) + ", the output was: " + str(outputz.name) + ", the fasta file used was: " + str(fastaQuery.name) + ", and the gene info tabse was:" + str(args.alldoer) + ".\n") # open log and print timestamp, inputs names, and output name.

# read fastaQuery
# now we do the same, but for the fasta that was used for blat. In that case, our dict will only have the name and sequence
reads_recorder = {} # dictionary to store sequences and names of reads
for item in SeqIO.parse(fastaQuery, "fasta"): #open fasta file and goes through each item
    reads_recorder[item.id] = item.seq # stores the sequence as the value to the id/name of the read


# read blat table
# read and organize input
#inputz = pd.read_csv(args.blat, sep='\t', header=None)# read input into a dataframe:
# give columns names to make life easier
# name columns
#columns=['0.match', '1.mismatch', '2.RepMatch', '3.Ns', '4.QGapCount', '5.QGapBases', '6.TGapCount', '7.TGapBases', '8.strand', '9.Qname[exon/intron]', '10.Qsize', '11.Qstart', '12.Qend', '13.Tname[read]', '14.Tsize', '15.Tstart', '16.Tend', '17.BlockCount', '18.BlockSizes', '19.qStarts', '20.tStarts', '21.Gene', '22.ExonIntronSeq', '23.Flags'])
inputz.columns=('match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'ReadName', 'ReadSize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts') # sets the names of the columns from the blat file
#alldoer.columns=('match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'ReadName', 'ReadSize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts') # sets the names of the columns from the blat file
# to add: '21.Gene', '22.ExonIntronSeq', '23.Flags', '24.QueryStarts-Ends', '25.DBStarts-Ends', '26.Sequence'
# remove columns we do not need/want
#del inputz['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'Qsize', 'BlockCount', 'qStarts', 'tStarts']
inputz.drop(['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts'], axis=1, inplace=True)
# add output columns/names
# add columns we will fill out later with a standard value (in this case, NA = Not Available)
inputz['QueryStarts-Ends'] = 'NA' # create a new column, and sets start-end in query
inputz['ReadStarts-Ends'] = 'NA' # create a new column, and sets start-ends in transcript
inputz['Gene'] = 'NA' # create a new column, and sets all values to NA
inputz['ExonIntronSeq'] = 'NA' # create a new column, and sets all values to NA
inputz['Sequence'] = 'NA' #create a new column, and sets all values to NA
inputz['Flags'] = 'NA' # create a new column, and sets all values to NA

UniqTranscripts = inputz['ReadName'].unique() # get uniq transcripts from input[:,13] -> i.e. 14th column

#TranscriptData = pd.DataFrame(columns = ['Tname', 'Gene', 'ExonIntronSeq', 'UniqID', 'Size', 'QStarts-Ends', 'DBStars-Ends', 'Flags', 'Sequence']) # initiates data frame for transcripts

outputz.write("Transcript\tTranscriptSize\tGene\tMullerElement\tChrm\tChrmStart-End\tExonIntronSeq\tEITranscStarts-Ends\tEIChrmStarts-Ends\tUniqID\t#Genes\t#Exons\t#Introns\tFlags\tSequence\n")# open output and print header

for transcript_name in UniqTranscripts: # for each uniq transcript:
    EIitems = [] # starts empty hash to store the exons/introns sequence
    EIloci = [] # starts an empty hash to store the loci (start-finish) of each match
    CEIloci = [] # starts an empty hash to store the loci (start-finish) of each match to chromosome
    Gene = [] # starts a hash to store the gene id of each match
    Flags = ""
    GenesNumb = 0
    IntronNumb = 0
    ExonNumb = 0
    InputSubset = inputz[inputz['ReadName'] == transcript_name] #subsets the full input only to the items that are from transcript transcript_name
    InputSubset.sort_values(['Tstart','Tend'], inplace=True) # sort according to Tstart first, and within that, accoridng to Tend
    for instance in range(len(InputSubset['ExonIntronSeq'])): # for each instance in the subset
        if "intron" in InputSubset['Qname'].iloc[instance]: # if it's an intron
            # intron names are quite complex, so we have to do a bunch of steps to get the gene it's a part of and between which exons it is. the general inscription goes: inton_GENE:Exon_GENE:Exon
            Intron, Set1, Set2 = InputSubset['Qname'].iloc[instance].split("_") # first we split the string wherever there's a "_", this will give us the word "intron", and the two gene:exon between which the intron in question is
            Gene1, EIitem1 = Set1.split(":") # now we split it between the gene name and the exon number
            Gene2, EIitem2 = Set2.split(":") # same
            InputSubset['ExonIntronSeq'].iloc[instance] = str(EIitem1) + "_" + str(EIitem2) # sets the ExonIntronSeq as the numeric representation of an intron
            IntronNumb += 1
            if Gene1 == Gene2: # if the two genes in the intron are the same...
                if not Gene: # if the Gene hash is empty
                    Gene = Gene1 # ...add that gene's name to the Gene category
                    GenesNumb += 1
                elif Gene1 in Gene: # if the hash is not empty, and the current gene is already stored in it
                    # do nothing
                    Gene = Gene
                else: # if the hash is not empty but the current gene is not in it
                    Gene = str(Gene) + "_" + str(Gene1) # concatenate the old gene id with the new one
                    GenesNumb += 1
                    if not Flags: # if the flags hash is empty
                        Flags = "DifferentGenes" # add the flag for different genes
                    elif "DifferentGenes" in Flags: # if flags is not empty but this item is already there
                        # do nothing
                        Flags = Flags
                    else: # if the flags hash is not empty, but doesn't have this item
                        Flags = Flags + ",DifferentGenes"
            else: # if genes are not the same...
                if not Gene: # if the Gene hash is empty
                    Gene = str(Gene1) + "_" + str(Gene2) # add both genes' name to the Gene category (separated by an _)
                    GenesNumb += 1
                elif (Gene1 in Gene) & (Gene2 in Gene): # if the hash is not empty, and both genes are already stored in it
                    # do nothing
                    Gene = Gene
                elif (Gene1 in Gene) & (Gene2 not in Gene): # if one gene is in the hahs but not the other
                    Gene = Gene + "_" + Gene2 # add just the gene that was not alsready in the hash
                    GenesNumb += 1
                elif (Gene2 in Gene) & (Gene1 not in Gene): # if the other gene is in the hahs but not the one
                    Gene = Gene + "_" + Gene1 # add just the gene that was not alsready in the hash
                    GenesNumb += 1
                else: # if the hash is not empty but the current gene is not in it
                    Gene = str(Gene) + "_" + str(Gene1) + "_" + str(Gene2) # concatenate the old gene id with the new ones
                    GenesNumb += 2
                if not Flags: # if the flags hash is empty
                    Flags = "DifferentGenes" # add the flag for different genes
                elif "DifferentGenes" in Flags: # if flags is not empty but this item is already there
                    # do nothing
                    Flags = Flags
                else: # if the flags hash is not empty, but doesn't have this item
                    Flags = Flags + ",DifferentGenes"
                if not Flags: # if there are no items in Flags
                    Flags = "IntronBetweenGenes" # add this flag to it
                elif "IntronBetweenGenes" in Flags: # if the flag is already in the hash
                    # do nothing
                    Flags = Flags
                else: # if the hash is not empty but doesn't have this item
                    Flags = Flags + ",IntronBetweenGenes" # add item to it
            if not Flags: # if there are no items in Flags
                Flags = "Intron"
            elif "Intron" in Flags: # if there's already the flag "intron" in the Flags hash, we don't need to do anything
                # do nothing
                Flags = Flags
            else: # if the flag "intron" is not in the Flags hash, we add it to the hash
                Flags = Flags + ",Intron"
        else: # if it's not an intron
            InputSubset['Gene'].iloc[instance], InputSubset['ExonIntronSeq'].iloc[instance] = InputSubset['Qname'].iloc[instance].split(":") # split the items name into the gene name and the exon number
            GenesNumb += 1
            ExonNumb += 1
            if not Gene: # if the Gene hash is empty
                Gene = InputSubset['Gene'].iloc[instance] # ...add that gene's name to the Gene category
                GenesNumb += 1
            elif str(InputSubset['Gene'].iloc[instance]) in Gene: # if the hash is not empty, and the current gene is already stored in it
                # do nothing
                Gene = Gene
            else: # if the hash is not empty but the current gene is not in it
                Gene = str(Gene) + "_" + str(InputSubset['Gene'].iloc[instance]) # concatenate the old gene id with the new one
                GenesNumb += 1
                if not Flags: # if the flags hash is empty
                    Flags = "DifferentGenes" # add the flag for different genes
                elif "DifferentGenes" in Flags: # if flags is not empty but this item is already there
                    # do nothing
                    Flags = Flags
                else: # if the flags hash is not empty, but doesn't have this item
                    Flags = Flags + ",DifferentGenes"
        InputSubset['QueryStarts-Ends'].iloc[instance] = str(InputSubset['Qstart'].iloc[instance]) + '-' + str(InputSubset['Qend'].iloc[instance]) # sets start-end in query
        InputSubset['ReadStarts-Ends'].iloc[instance] = str(InputSubset['Tstart'].iloc[instance]) + '-' + str(InputSubset['Tend'].iloc[instance]) # sets start-ends in transcript
        if not alldoer[alldoer.Gene==str(Gene)].empty: # if the gene is present in our absolute table
            GeneInfo = alldoer[alldoer.Gene==str(Gene)] #get gene from absolute table
            Muller = GeneInfo.MullerElement.iloc[0] # get the info we want.
            Chrm = GeneInfo.Chromosome.iloc[0]
            Cor = GeneInfo.Colour.iloc[0]
            CorDe = GeneInfo.ColourFrom.iloc[0] #type of cell the data is from
            GeneLocus = GeneInfo.GeneLoci.iloc[0]
            AgeZ = GeneInfo.AgeZhang.iloc[0]
            AgeA = GeneInfo.AgeAssis.iloc[0]
            GeneEI = GeneInfo.SimpleEISeq.str.split(",") #sequence of exons introns that belong ta that gene
            GeneCEISE = GeneInfo.ExonIntronLociInChromosome.str.split(",") #location of said exons and introns
            if GeneCEISE[GeneEI==InputSubset['ExonIntronSeq'].iloc[instance]].any(): #if the location is available
                SubSetEIseq = GeneCEISE[GeneEI==InputSubset['ExonIntronSeq'].iloc[instance]] # get location  of exons/introns we also found in our transcript
                TempChrmStart = int(SubSetEIseq.split("-")[0]) + int(InputSubset['Qstart'].iloc[instance])
                TempChrmEnd = int(SubSetEIseq.split("-").iloc[1]) + int(InputSubset['Qend'].iloc[instance])
                TempChrmStartEnd = str(TempChrmStart) + "-" + str(TempChrmEnd)
            else: #if there's no info, it gets an "NA"
                TempChrmStartEnd = "NA"
        else: #if we don't have more info on the gene, everything gets an "NA"
            Muller = "NA"
            Chrm = "NA"
            Cor = "NA"
            CorDe = "NA"
            GeneLocus = "NA"
            AgeZ = "NA"
            AgeA = "NA"
            GeneEI = "NA"
            GeneCEISE = "NA"
            SubSetEIseq = "NA"
            TempChrmStartEnd = "NA"
        if not EIitems: # if there are no items in the hash
            EIitems =  InputSubset['ExonIntronSeq'].iloc[instance] # add the item to the sequence hash
            EIloci =  InputSubset['ReadStarts-Ends'].iloc[instance] # add start-end to the start-end hash
            CEIloci =  TempChrmStartEnd # add chrm start-end to the chrm start-end hash
            QEIloci =  InputSubset['QueryStarts-Ends'].iloc[instance] # add query start-end to the query start-end hash
        else: # if the hash is not empty
            EIitems =  str(EIitems) + ',' + str(InputSubset['ExonIntronSeq'].iloc[instance]) # concatenate the new item to the old ones
            EIloci =  str(EIloci) + ',' + str(InputSubset['ReadStarts-Ends'].iloc[instance]) # same
            CEIloci = str(CEIloci) + "," + str(TempChrmStartEnd) #same
            QEIloci =  str(QEIloci) + ',' + str(InputSubset['QueryStarts-Ends'].iloc[instance]) # same
    outputz.write(str(InputSubset['ReadName'].iloc[0]) + #Transcript Name
                  "\t" + str(InputSubset['ReadSize'].iloc[0]) + #Transcript Size
                  "\t" + str(Gene) + #Gene Name
                  "\t" + str(Muller) + #Muller Element where gene is
                  "\t" + str(Chrm) + #Chromosome where Gene is
                  "\t" + str(GeneLocus) + #GeneLoci in Chromosome
                  "\t" + str(EIitems) +# Exon/Intron Sequence
                  "\t" + str(EIloci) + #Loci of match of Exons/Introns in Transcrcipt
                  "\t" + str(CEIloci) + #Loci of match of Exons/Introns in Chrm
                  "\t" + str(AgeZ) + #Age according to Zhang et al 2010
                  "\t" + str(AgeA) + #Ageaccording to Assis & Bachtrog 2013
                  "\t" + str(Cor) + #Chromatin Color at gene location in either BG3 (preferable) or S2
                  "\t" + str(CorDe) + #Cell type chromati colour was acquired from
                  "\t" + str(Gene) + "." + str(EIitems) + #unique ID of transcript sequence
                  "\t" + str(GenesNumb) + #Number of genes matched to trannscript
                  "\t" + str(ExonNumb) + #Number of exons in transcript
                  "\t" + str(IntronNumb) + #Number of introns in transcript
                  "\t" + str(Flags) + #flags for errors found during script
                  "\t" + str(reads_recorder[InputSubset['ReadName'].iloc[0]]) + #transcript sequence
                  "\n") # prints all important things to the output

#outputz.write("tTranscrip\tSize\tGene\tMullerElement\tChrm!*\tChrmStart-End\tExonIntronSeq\tEITranscStarts-Ends\tEIChrmStarts-Ends!*\tAgeZhang\tAgeAssis\tChromatinColour\tCellTypeOfColour\tUniqID\t#Genes\t#Exons\t#Introns\tFlags\tSequence\n")# open output and print header
# close every used file
outputz.close()# close output
log.close() # closes log
#inputz.close() # closes blat file
# end




