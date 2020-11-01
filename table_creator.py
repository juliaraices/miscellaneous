#!bin/usr/python3
# import packages we will need to work with dataframes and all
import sys, argparse, os # import packages to call command line commands, to parse arguments given when calling the program
from Bio import SeqIO # import part of the Bio package that deals with input and output of sequences/fasta/fastq/etc
import numpy as np # imports numpy for dealing with numbers and stats
import pandas as pd # pandas is for dealing with dataframes
pd.options.mode.chained_assignment = None  # default='warn' # changes the options for pandas so it doesn't give warnings for everything. in other words: I'm bad and don't want to know about it =\
from datetime import datetime # allows us to add the date/time to the code/output

# Read arguments (file names)
# allows to create an automatic message for usage and checks if all the parameters have been provided, or give the default input for each parameter that has a default value/file
parser = argparse.ArgumentParser(description='Program to create a table with the list of introns/exons that comprise different reads.') # sets the description for the full program, in case it's called with no arguments
parser.add_argument("--blat", required=True, type=str, help='Output from blat of reads against introns and exons') # states a required argument, a blat file, and has a helper message in case you don't provide it, or ask for help
parser.add_argument("--fasta", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/dmel_exon_intron.fasta", type=str, help='Fasta file used in blat. Default is the file with exons and introns in Drosophila melanogaster') # sets the default fasta file to be used in case it is not provided by the user
parser.add_argument("--output", default="IntronExonTable.output", help="Desired name for the output file. Default is IntronExonTable.output", type=str) # sets the output file name if none is given. If there's already a file with that name, it will be overwritten.
parser.add_argument("--log", default="TableMaker.log", help="Desired name for the log file. Default is TableMaker.log", type=str) # sets the log file name if none is given. The new log will be appended to the end of the given file.

args = parser.parse_args() # stores arguments given in args, so we can reference them.

try: # makes sure you can open all the files
    log = open(args.log, "a") # "a" will append to the end of the file
    # open input
    inputz = open(args.blat, "r") # opens file as read only
    fastaz = open(args.fasta, "r") # opens file as read only
    outputz = open(args.output, "w") # "w" will overwrite file
# If files do not open:
except FileNotFoundError or IOError: # if any of the files is not openned, shuts down the program and logs the errors
    # report to log
    log.write("One or more of the files given was not available.\n") # prints error to log
    print("File name is not valid. Please try again.") # prints error to standard output
    # exit program with erros
    sys.exit("Files are not valid.") # prints error as system error and leaves the program

outputz.write("Transcript\tGene\tExonIntronSeq\tUniqID\tTranscriptSize\tQueryStarts-Ends\tDBStarts-Ends\tFlags\tSequence\n")# open output and print header

log.write("\n\n#########################\nNew usage of table_creator.py at " + str(datetime.now()) + ".\n\t The input used was " + str(inputz.name) + ", the output was: " + str(outputz.name) + ", and the fasta file used was:" + str(fastaz.name) + ".\n") # open log and print timestamp, inputs names, and output name.

seq_records = SeqIO.to_dict(SeqIO.parse(fastaz, "fasta")) #open fasta file and store its info

inputz = pd.read_csv(args.blat, sep='\t', header=None)# read input into a dataframe:
# give columns names to make life easier
#columns=['0.match', '1.mismatch', '2.RepMatch', '3.Ns', '4.QGapCount', '5.QGapBases', '6.TGapCount', '7.TGapBases', '8.strand', '9.Qname[exon/intron]', '10.Qsize', '11.Qstart', '12.Qend', '13.Tname[read]', '14.Tsize', '15.Tstart', '16.Tend', '17.BlockCount', '18.BlockSizes', '19.qStarts', '20.tStarts', '21.Gene', '22.ExonIntronSeq', '23.Flags'])
inputz.columns = ['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'Tname', 'Tsize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts'] # sets the names of the columns from the blat file
# to add: '21.Gene', '22.ExonIntronSeq', '23.Flags', '24.QueryStarts-Ends', '25.DBStarts-Ends', '26.Sequence'
# add columns we will fill out later with a standard value (in this case, NA = Not Available)
inputz['Gene']="NA" # create a new column, and sets all values to NA
inputz['ExonIntronSeq']="NA" # create a new column, and sets all values to NA
inputz['Size']="NA" # create a new column, and sets all values to NA
inputz['Flags']="NA" # create a new column, and sets all values to NA
inputz['QueryStarts-Ends']="NA" # create a new column, and sets all values to NA
inputz['DBStarts-Ends']="NA" # create a new column, and sets all values to NA
inputz['Sequence']="NA" #create a new column, and sets all values to NA

UniqTranscripts = inputz['Tname'].unique() # get uniq transcripts from input[:,13] -> i.e. 14th column
# makes a new data frame to put what will be outputed
FinalPrint = pd.DataFrame(columns = ['Tname', 'Gene', 'ExonIntronSeq', 'UniqID', 'Size', 'QStarts-Ends', 'DBStars-Ends', 'Flags', 'Sequence']) # initiates data frame for transcripts

for transcript_name in UniqTranscripts: # for each uniq transcript:
    EIdata={} # initiate an empty hash to store things in
    flag = "" # initiate an empty flag item
    TranscriptData = pd.DataFrame(columns = ['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'Tname', 'Tsize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts', 'Gene', 'ExonIntronSeq', 'Starts-Ends', 'Flags']) # initiates temporary data frame for transcript
    # get all apearances of it in input
    InputSubset = inputz[inputz['Tname'] == transcript_name] # makes a temporary variable only with the one read/transcript
    InputSubset.sort_values(['Tstart','Tend'], inplace=True) # sort according to Tstart first, and within that, accoridng to Tend
    for transcript_instance in range(len(InputSubset)): # for each instace of that transcript
        if "intron" in InputSubset['Qname'].iloc[transcript_instance]: # check if it's an intron:
            # if read has intron, make an error alert
            log.write("\t Error: INTRON alert. The "+InputSubset['Tname'].iloc[transcript_instance]+" has the following match, "+InputSubset['Qname'].iloc[transcript_instance]+", that is an intron.\n") # writes to the log that there was an intron (form: intron_FBgn#:#_FBgn#:#)
            Intron_FBgn1, IntronStart_FBgn2, IntronEnd = InputSubset['Qname'].iloc[transcript_instance].split(":") # divide intron name, so we can see the genes and introns involoved
            IntronStart, Gene2 = IntronStart_FBgn2.split("_") # subdivides the intron's name again to get the actual gene name
            EIitem = IntronStart+"_"+IntronEnd # sets the exons between which the exon is
            WordIntron, Gene1 = Intron_FBgn1.split("_") # gets the second gene's id
            if Gene1 != Gene2: # if any of the named genes is different from each other, that is bad and we address it
                log.write("\t\t Error: Intron between different genes in "+InputSubset['Qname'].iloc[transcript_instance]+" for read"+InputSubset['Tname'].iloc[transcript_instance]+"!!!\n") # write the genes and trancript with the intron between genes <o>
                NewGene=Gene1+"_"+Gene2 # sets the name of the gene as the names of both genes that comprise it.
                if flag == "": # add flag to empty flag variable
                    flag = "z" # add the flag that means intron between different genes
                elif not ("z" in flag): # if the flag variable is not empty and doesn't have a "z" flag
                    flag = flag+",z" # adds "z" to the flag variable
            else: # i.e. if the genes that comprise the exon are the same
                NewGene=Gene1 #sets the new gene to be added
                if flag == "": # adds flag for intron if the flag variable is empty
                    flag = "w" # "w" is the flag for "normal" introns""
                elif not "w" in flag: # if the flag variable is not empty, but doesn't already have a "w"
                    flag = flag+",w" # adds "w" to flags
        # parse name/genes
        else: # if read has no intron ^^
            NewGene, EIitem = InputSubset['Qname'].iloc[transcript_instance].split(":") # gets the name of the gene and exon that comprises that bit
        if TranscriptData.empty: # if the new hash is empty we add things the easiest way ;)
            TranscriptData = TranscriptData.append(InputSubset.iloc[transcript_instance]) # adds this instance to the transcripts database
            TranscriptData['Gene'].iloc[0] = NewGene # adds new gene name to the transcripts hash
            TranscriptData['ExonIntronSeq'].iloc[0] = EIitem # adds intron/exon item to transcripts hash
        elif not NewGene in TranscriptData['Gene'].iloc[0]: # if the new hash is not empty and the gene we found is not in the new hash gene name
            if "_" in NewGene: # if more than one gen comprises the already known genes in the transcript (their names are separated with _ )
                NewGenes2 = NewGenes.split("_") # split where there's a _
                for k in range(len(NewGenes2)): # gfor each gene splited above
                    if not NewGenes2[k] in NewHash['Gene'].iloc[0]: # if the splited gene is not in the stored ones
                        NewHash['Gene'].iloc[0] = NewHash['Gene'].iloc[0]+"_"+NewGenes2[k] # adds splited gene to stored ones
            else: # if the stored gene is just one gene (doesn't have a _)
                NewHash['Gene'].iloc[0] = NewHash['Gene'].iloc[0]+"_"+NewGenes # just adds the new gene to the stored ones
            if flag == "": # if the flag variable is empty
                flag = "y" # add "y" to the flags
            elif not "y" in flag: # if flag variable is not empty but doesn't have the "y" flag
                flag = flag+",y" # adds the "y" flag to it
            #NewHash['ExonIntronSeq'].iloc[0] = NewHash['ExonIntronSeq'].iloc[0]+","+NewItem
        #else:
            #NewHash['ExonIntronSeq'].iloc[0] = NewHash['ExonIntronSeq'].iloc[0]+","+NewItem
        # if Qstart > Qend
        if (temp['Tstart'].iloc[j] > temp['Tend'].iloc[j]): #
            log.write("\t Error: "+temp['Qname'].iloc[j]+" had start bigger than end in the "+temp['Tname'].iloc[j]+".\n")
            if flag == "":
                flag = "a"
            elif not "a" in flag:
                flag = flag+",a"
        # possibiblities where new is inside old sequences:
        # get starts and ends of previous 
        thisOne = EIfasta[temp['Qname'].iloc[j]]
        StartChr, EndChr = thisOne.split(":")[1].split("..")
        TrueStart = int(''.join(s for s in StartChr if s.isdigit()))+int(temp['Qstart'].iloc[j])
        TrueEnd = int(''.join(s for s in EndChr if s.isdigit()))+int(temp['Qend'].iloc[j])
        SE = str(TrueStart)+"-"+str(TrueEnd)
   #     print(SE+"\n")
        if NewHash['Starts-Ends'].iloc[0] == "NA":
            NewHash['Starts-Ends'].iloc[0] = SE
            NewHash['ExonIntronSeq'].iloc[0] = NewItem
        else:
            eita = "n"
            SplintersSE = NewHash['Starts-Ends'].iloc[0].split(",")
            SplintersI = NewHash['ExonIntronSeq'].iloc[0].split(",")
            for m in range(len(SplintersSE)):
                if (SplintersSE[m]==SE) and (SplintersI[m]==NewItem):
                    log.write("Same match, ("+str(NewItem)+") appeared more than once for read "+temp['Tname'].iloc[j]+" in the same place ("+SE+").\n")
                    eita="y"
                    if flag == "":
                        flag = "b"
                    elif not "b" in flag:
                        flag = flag+",b"
                elif SplintersI[m]==NewItem:
                    log.write("Same match, ("+str(NewItem)+") appeared more than once for read "+temp['Tname'].iloc[j]+" in different places ("+SE+", and "+SplintersSE[m]+").\n")
                    eita="y"
                    if flag == "":
                        flag = "c"
                    elif not "c" in flag:
                        flag = flag+",c"
                elif SplintersSE[m]==SE:
                    log.write("Different matches, ("+str(NewItem)+" and "+str(SplintersI[m])+") appeared in the same place ("+SE+") for read "+temp['Tname'].iloc[j]+".\n")
                    eita="y"
                    if flag == "":
                        flag = "d"
                    elif not "d" in flag:
                        flag = flag+",d"
            if eita != "y":
                NewHash['Starts-Ends'].iloc[0] = NewHash['Starts-Ends'].iloc[0]+","+SE
                NewHash['ExonIntronSeq'].iloc[0] = NewHash['ExonIntronSeq'].iloc[0]+","+str(NewItem)
    StarkEnds=NewHash['Starts-Ends'].iloc[0].split(",")
    StarkItems=NewHash['ExonIntronSeq'].iloc[0].split(",")
    Sansa = pd.DataFrame()#columns=['start', 'end', 'length', 'item'])
    for p in range(len(StarkEnds)):
        inicio, fim = StarkEnds[p].split("-")
        tamanho = int(fim) - int(inicio)
        temporery = [inicio, fim, tamanho, StarkItems[p]]
        Sansa = Sansa.append([temporery], ignore_index=True)
    Sansa.columns=['start', 'end', 'length', 'item']
    sansadrop = list()
    for o in range(len(Sansa)):
        Arya = Sansa.drop(Sansa.index[o])
        for m in range(len(Arya)):
            if ((Arya['start'].iloc[m]>=Sansa['start'].iloc[o]) and (Arya['end'].iloc[m]<=Sansa['end'].iloc[o])):
                # Arya smaller than Sansa and contained in it
                # Arya and sansa cover exactly the same area
                #sansadrop = sansadrop
                eita = 1+10
            elif ((Sansa['start'].iloc[o]>=Arya['start'].iloc[m]) and (Sansa['end'].iloc[o]<=Arya['end'].iloc[m])):
                # Sansa smaller than Arya and contained in it
                if (not o in sansadrop) and (not m in sansadrop) and Sansa['length'].iloc[o] >= 100:
                    sansadrop.append(o)
            elif (Arya['start'].iloc[m]>=Sansa['start'].iloc[o]) and (Arya['end'].iloc[m]>=Sansa['end'].iloc[o]):
                # Arya starts after Sansa starts, and ends after Sansa ends.
                # Arya starts after Sansa start, and ends where sansa ends.
                # Arya starts where Sansa starts, and ends where sansa ends.
                overlap = int(Sansa['end'].iloc[o]) - int(Arya['start'].iloc[m])
                if (not o in sansadrop) and (not m in sansadrop) and overlap>=100:
                    sansadrop.append(o)
            elif (Arya['start'].iloc[m]<=Sansa['start'].iloc[o]) and (Arya['end'].iloc[m]<=Sansa['end'].iloc[o]):
                # Arya starts where sansa starts, and ends after sansa ends.
                # Arya starts before Sansa starts, and ends before Sansa ends
                # Arya starts before Sansa starts, and ends where Sansa ends.
                # Arya starts where Sansa starts, and ends before Sansa ends.
                # calculate overlap:
                overlap = int(Arya['end'].iloc[m]) - int(Sansa['start'].iloc[o])
                if (not o in sansadrop) and (not m in sansadrop) and overlap>=100:
                    sansadrop.append(o)
            elif ((Arya['start'].iloc[m]<Sansa['start'].iloc[o]) and (Arya['end'].iloc[m]<=Sansa['start'].iloc[o]) or (Arya['start'].iloc[m]>=Sansa['end'].iloc[o] and Arya['end'].iloc[m]>Sansa['end'].iloc[o])):
                # Arya starts and ends before sansa starts
                # Arya starts and ends after sansa ends
                #ansadrop=sansadrop
                eita = 1+13
            else:
                print("Something has gone terribly wrong!!! <o>"+str(Arya['start'].iloc[m])+" "+str(Arya['end'].iloc[m])+"\t"+str(Sansa['start'].iloc[o])+" "+str(Sansa['end'].iloc[o])+"\n")
    if sansadrop!=[]:
        Sansa = Sansa.drop(Sansa.index[sansadrop])
    StarkSE = pd.DataFrame(columns=['SE'])
    StarkI = pd.DataFrame(columns=['I'])
    for q in range(len(Sansa)):
        NewSE = str(Sansa['start'].iloc[q])+"-"+str(Sansa['end'].iloc[q])
        if q == 0:
            StarkSE = str(NewSE)
            StarkI = str(Sansa['item'].iloc[q])
        else:
            StarkSE = str(StarkSE)+","+str(NewSE)
            StarkI = str(StarkI)+","+str(Sansa['item'].iloc[q])
    NewHash['Starts-Ends'] = StarkSE
    NewHash['ExonIntronSeq'] = StarkI
    NewHash['Flags'].iloc[0]=flag # add flags to hash
    # make PrintingHash NewItem with Qname, Tname, and flags
    FinalPrint = FinalPrint.append([NewHash], ignore_index=True) # add new item to end of hash

#FinalPrint.to_string(outputz, header=True, index=False)
for i in range(len(FinalPrint)): # for each item in the FinalPrint hash
    outputz.write(str(FinalPrint['Tname'].iloc[i])+"\t"+str(FinalPrint['Gene'].iloc[i])+"\t"+str(FinalPrint['ExonIntronSeq'].iloc[i])+"\t"+str(FinalPrint['Starts-Ends'].iloc[i])+"\t"+str(FinalPrint['Flags'].iloc[i])+"\n") # print database to output

outputz.close()# close output
# print number of errors, number of reads, number of flags reported, and flags itself to log
log.write("\n\n") # creates space between 
log.close() # closes log
# end
