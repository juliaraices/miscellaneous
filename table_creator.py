#!bin/usr/python3
## import packages we will need to work with dataframes and all
import sys, argparse, os # import packages to call command line commands, to parse arguments given when calling the program
from Bio import SeqIO # import part of the Bio package that deals with input and output of sequences/fasta/fastq/etc
import numpy as np # imports numpy for dealing with numbers and stats
import pandas as pd # pandas is for dealing with dataframes
pd.options.mode.chained_assignment = None  # default='warn' # changes the options for pandas so it doesn't give warnings for everything. in other words: I'm bad and don't want to know about it =\
from datetime import datetime # allows us to add the date/time to the code/output

## Read arguments (file names)
# allows to create an automatic message for usage and checks if all the parameters have been provided, or give the default input for each parameter that has a default value/file
parser = argparse.ArgumentParser(description='Program to create a table with the list of introns/exons that comprise different reads.') # sets the description for the full program, in case it's called with no arguments
parser.add_argument("--blat", required=True, type=str, help='Output from blat of reads against introns and exons') # states a required argument, a blat file, and has a helper message in case you don't provide it, or ask for help
parser.add_argument("--query", required=True, type=str, help='Reads/data used in blat against introns and exons') # states a required argument, a fasta file, and has a helper message in case you don't provide it, or ask for help
parser.add_argument("--db", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/dmel_exon_intron.fasta", type=str, help='Fasta file used in blat. Default is the file with exons and introns in Drosophila melanogaster') # sets the default fasta file to be used in case it is not provided by the user
parser.add_argument("--output", default="IntronExonTable.output", help="Desired name for the output file. Default is IntronExonTable.output", type=str) # sets the output file name if none is given. If there's already a file with that name, it will be overwritten.
parser.add_argument("--log", default="TableMaker.log", help="Desired name for the log file. Default is TableMaker.log", type=str) # sets the log file name if none is given. The new log will be appended to the end of the given file.

args = parser.parse_args() # stores arguments given in args, so we can reference them.

## open arguments/files
try: # makes sure you can open all the files
    log = open(args.log, "a") # "a" will append to the end of the file
    # open input
    inputz = open(args.blat, "r") # opens file as read only
    fastaz = open(args.db, "r") # opens file as read only
    fastaz_query = open(args.query, "r") # opens file as read only
    outputz = open(args.output, "w") # "w" will overwrite file
# If files do not open:
except FileNotFoundError or IOError: # if any of the files is not openned, shuts down the program and logs the errors
    # report to log
    log.write("One or more of the files given was not available.\n") # prints error to log
    print("File name is not valid. Please try again.") # prints error to standard output
    # exit program with erros
    sys.exit("Files are not valid.") # prints error as system error and leaves the program

# write the used files and when it was started
log.write("\n\n#########################\nNew usage of table_creator.py at " + str(datetime.now()) + ".\n\t The input used was " + str(inputz.name) + ", the output was: " + str(outputz.name) + ", and the fasta file used was:" + str(fastaz.name) + ".\n") # open log and print timestamp, inputs names, and output name.

seq_recorder = {} #make empty dict to store fasta sequences and data:
# from the fasta file get location, length and type, if they are available.
for item in SeqIO.parse(fastaz, "fasta"): #open fasta file and goes through each item
    item_gene = item.id.split(":")[0] #split the id for the item, and stores the name of the gene (ignores the exon/intron part)
    description_items = item.description.split(";") # splits the description of the item. description is where the SeqIO will store everything it doesn't know what is
    for characteristic in range(len(description_items)): # for each part in the description
        if "type" in description_items[characteristic]: # if the part in questions is the type, we want it
            item_type = description_items[characteristic].split("=")[1] # so, we split it in the = sign, and store it
        elif "length" in description_items[characteristic]: # if the part in questions is the length, we want it
            item_length = description_items[characteristic].split("=")[1]
        elif "loc" in description_items[characteristic]: # if the part in questions is the location (ie loc), we want it
            loc = description_items[characteristic].split("=")[1].split(":")
            item_chromosome = loc[0]
            item_chromosomalLoci = loc[1]
    seq_recorder[item.id] = {'sequence':item.seq, 'type':item_type, 'chromosome':item_chromosome, 'loci':item_chromosomalLoci, 'length':item_length, 'gene':item_gene}

# stores all that to use later, so we can check with the things we matched with blat

# now we do the same, but for the fasta that was used for blat. In that case, our dict will only have the name and sequence
reads_recorder = {} # dictionary to store sequences and names of reads
for item in SeqIO.parse(fastaz_query, "fasta"): #open fasta file and goes through each item
    reads_recorder[item.id] = item.seq # stores the sequence as the value to the id/name of the read

# read and organize input
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
    EIdata=[] # initiate an empty hash to store things in
    flag = "" # initiate an empty flag item
    TranscriptData = pd.DataFrame(columns = ['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'Tname', 'Tsize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts', 'Gene', 'ExonIntronSeq', 'Starts-Ends', 'Flags']) # initiates InputSubsetorary data frame for transcript
    # get all apearances of it in input
    InputSubset = inputz[inputz['Tname'] == transcript_name] # makes a InputSubsetorary variable only with the one read/transcript
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
                NewGeneS = NewGene.split("_") # split where there's a _
                for SubGene in range(len(NewGeneS)): # gfor each gene splited above
                    if not NewGeneS[SubGene] in TranscripitData['Gene'].iloc[0]: # if the splited gene is not in the stored ones
                        TranscriptData['Gene'].iloc[0] = TranscriptData['Gene'].iloc[0]+"_"+NewGeneS[SubGene] # adds splited gene to stored ones
            else: # if the stored gene is transcript_instanceust one gene (doesn't have a _)
                TranscriptData['Gene'].iloc[0] = TranscriptData['Gene'].iloc[0]+"_"+NewGene # transcript_instanceust adds the new gene to the stored ones
            if flag == "": # if the flag variable is empty
                flag = "y" # add "y" to the flags
            elif not "y" in flag: # if flag variable is not empty but doesn't have the "y" flag
                flag = flag+",y" # adds the "y" flag to it
            #TranscriptData['ExonIntronSeq'].iloc[0] = TranscriptData['ExonIntronSeq'].iloc[0]+","+EIitem
        #else:
            #TranscriptData['ExonIntronSeq'].iloc[0] = TranscriptData['ExonIntronSeq'].iloc[0]+","+EIitem
        # if Qstart > Qend
        if (InputSubset['Tstart'].iloc[transcript_instance] > InputSubset['Tend'].iloc[transcript_instance]): # if the match start is higher than it's end
            log.write("\t Error: "+InputSubset['Qname'].iloc[transcript_instance]+" had start bigger than end in the "+InputSubset['Tname'].iloc[transcript_instance]+".\n") # adds the instance and match to log
            if flag == "": # in case the flag variable is empty
                flag = "a" # add "a" to flag, which means it has a match with a start bigger than the end
            elif not "a" in flag: # if the flag variable is not empty and does not have an a
                flag = flag+",a" # add "a" to it
        # possibiblities where new is inside old sequences:
        # get starts and ends of previous 
        #thisOne = EIitem[InputSubset['Qname'].iloc[transcript_instance]] # 
        #StartChr, EndChr = thisOne.split(":")[1].split("..") #
        #TrueStart = int(''.transcript_instanceoin(s for s in StartChr if s.isdigit()))+int(InputSubset['Qstart'].iloc[transcript_instance]) #
        #TrueEnd = int(''.transcript_instanceoin(s for s in EndChr if s.isdigit()))+int(InputSubset['Qend'].iloc[transcript_instance]) #
        SE = str(InputSubset['Tstart'].iloc[transcript_instance])+"-"+str(InputSubset['Tend'].iloc[transcript_instance]) # adds the start and end of match
        #print(SE+"\n")
        if TranscriptData['Starts-Ends'].iloc[0] == "NA": # if there's no start-end set
            TranscriptData['Starts-Ends'].iloc[0] = SE # set new start-end with  new ones
            TranscriptData['ExonIntronSeq'].iloc[0] = EIitem # set exon intron sequence with new ones
        else: # if start-end was not yet set
            eita = "n" ## sets new flag
            SplintersSE = str(TranscriptData['Starts-Ends'].iloc[0]).split(",") # split starts and ends of trnascript
            SplintersI = TranscriptData['ExonIntronSeq'].iloc[0].split(",") # split exons and introns
            for m in range(len(SplintersSE)): # for each item in the hash
                if (SplintersSE[m]==SE) and (SplintersI[m]==EIitem): #if the new item and the SE item are the same
                    log.write("Same match, ("+str(EIitem)+") appeared more than once for read "+InputSubset['Tname'].iloc[transcript_instance]+" in the same place ("+SE+").\n") # write to log whicch item is the same
                    eita="y" # change flag variable
                    if flag == "": # if the flag variable is empty
                        flag = "b"  # add "b" to flag
                    elif not "b" in flag: # if the flag variable is not empty and does not have a b
                        flag = flag+",b" # add b to flag
                elif SplintersI[m]==EIitem: # if new item already in hash
                    log.write("Same match, ("+str(EIitem)+") appeared more than once for read "+InputSubset['Tname'].iloc[transcript_instance]+" in different places ("+SE+", and "+SplintersSE[m]+").\n") # write error to log
                    eita="y" # change flag variable
                    if flag == "":  # if the flag variable is empty
                        flag = "c"  # add c to flag
                    elif not "c" in flag: # if the flag variable is not empty and does not have a c
                        flag = flag+",c"  # add c to flag
                elif SplintersSE[m]==SE: # if item already in hash
                    log.write("Different matches, ("+str(EIitem)+" and "+str(SplintersI[m])+") appeared in the same place ("+SE+") for read "+InputSubset['Tname'].iloc[transcript_instance]+".\n") # write error to log
                    eita="y" # change flag variable
                    if flag == "": # if the flag variable is empty
                        flag = "d" # add d to flag
                    elif not "d" in flag: # if the flag variable is not empty and does not have a d
                        flag = flag+",d" # add d to flag
            if eita != "y": # if flag is "y"
                TranscriptData['Starts-Ends'].iloc[0] = str(TranscriptData['Starts-Ends'].iloc[0])+","+str(SE) #add start-end to transcript data hash
                TranscriptData['ExonIntronSeq'].iloc[0] = str(TranscriptData['ExonIntronSeq'].iloc[0])+","+str(EIitem) # add newitems to transcript data hash
#    StarkEnds=TranscriptData['Starts-Ends'].iloc[0].split(",") # split all stasts and ends in hash item
#    StarkItems=TranscriptData['ExonIntronSeq'].iloc[0].split(",") # split all introns/exons in the hash item
#    Sansa = pd.DataFrame()#columns=['start', 'end', 'length', 'item']) # make empty dataframe
#    for p in range(len(StarkEnds)): # for each item in StarkEnds
#        inicio, fim = StarkEnds[p].split("-") # gets the values from start and end, to calculate size
#        tamanho = int(fim) - int(inicio) # calculates the sizer of the item
#        InputSubsetorery = [inicio, fim, tamanho, StarkItems[p]] # make snew hash with data collected before
#        Sansa = Sansa.append([InputSubsetorery], ignore_index=True) # add to hahs
#    Sansa.columns=['start', 'end', 'length', 'item'] # set the names of the columns in sansa
#    sansadrop = list() # create an empty list
#    for o in range(len(Sansa)): # for each item in sansa
#        Arya = Sansa.drop(Sansa.index[o]) # remove the current item from sansa and make it into a new hash
#        for m in range(len(Arya)): # for each item in arya
#            if ((Arya['start'].iloc[m]>=Sansa['start'].iloc[o]) and (Arya['end'].iloc[m]<=Sansa['end'].iloc[o])): # if arya starts after sansa and ends before it
                # Arya smaller than Sansa and contained in it
                # Arya and sansa cover exactly the same area
                #sansadrop = sansadrop
#                eita = 1+10 #makes the eita variable into 14. why? idk... (yet))
#            elif ((Sansa['start'].iloc[o]>=Arya['start'].iloc[m]) and (Sansa['end'].iloc[o]<=Arya['end'].iloc[m])): # if arya starts after sansa and ends before sansa does
                # Sansa smaller than Arya and contained in it
#                if (not o in sansadrop) and (not m in sansadrop) and Sansa['length'].iloc[o] >= 100: # if neither of the items is listed to be droped
#                    sansadrop.append(o) # append item in question to the list of items to drop
#            elif (Arya['start'].iloc[m]>=Sansa['start'].iloc[o]) and (Arya['end'].iloc[m]>=Sansa['end'].iloc[o]): # if arya starts after sansa, and ends after sansa ends
                # Arya starts after Sansa starts, and ends after Sansa ends.
                # Arya starts after Sansa start, and ends where sansa ends.
                # Arya starts where Sansa starts, and ends where sansa ends.
#                overlap = int(Sansa['end'].iloc[o]) - int(Arya['start'].iloc[m]) # calculates overlap between two items
#                if (not o in sansadrop) and (not m in sansadrop) and overlap>=100: # if neither of the items is listed to be droped
#                    sansadrop.append(o) # append item in question to the list of items to drop
#            elif (Arya['start'].iloc[m]<=Sansa['start'].iloc[o]) and (Arya['end'].iloc[m]<=Sansa['end'].iloc[o]):  # if arya starts before sansa does, and ends before sansa does 
                # Arya starts where sansa starts, and ends after sansa ends.
                # Arya starts before Sansa starts, and ends before Sansa ends
                # Arya starts before Sansa starts, and ends where Sansa ends.
                # Arya starts where Sansa starts, and ends before Sansa ends.
                # calculate overlap:
#                overlap = int(Arya['end'].iloc[m]) - int(Sansa['start'].iloc[o]) # calculates overlap between two items
#                if (not o in sansadrop) and (not m in sansadrop) and overlap>=100: # if neither of the items is listed to be droped
#                    sansadrop.append(o) # append item in question to the list of items to drop 
#            elif ((Arya['start'].iloc[m]<Sansa['start'].iloc[o]) and (Arya['end'].iloc[m]<=Sansa['start'].iloc[o]) or (Arya['start'].iloc[m]>=Sansa['end'].iloc[o] and Arya['end'].iloc[m]>Sansa['end'].iloc[o])): # if teh start of one is before the other, and the end of one is also before the start of the other, or starts after the other ends, and the one aends after the other endzs too.
                # Arya starts and ends before sansa starts
                # Arya starts and ends after sansa ends
                #ansadrop=sansadrop
#                eita = 1+13 #makes the eita variable into 14. why? idk... (yet)
#            else: # if no other applies, do this1
#                print("Something has gone terribly wrong!!! <o>"+str(Arya['start'].iloc[m])+" "+str(Arya['end'].iloc[m])+"\t"+str(Sansa['start'].iloc[o])+" "+str(Sansa['end'].iloc[o])+"\n") # print error to strandard output
#    if sansadrop!=[]: # if sansadrop is not empty
#        Sansa = Sansa.drop(Sansa.index[sansadrop]) #sansa drops the item sansadrop
#    StarkSE = pd.DataFrame(columns=['SE']) # starkse is a dataframe with one column
#    StarkI = pd.DataFrame(columns=['I']) # starki is a dataframe with one column
#    for q in range(len(Sansa)): # for item in sansa
#        NewSE = str(Sansa['start'].iloc[q])+"-"+str(Sansa['end'].iloc[q]) # # sets NewSE as the start and end in Sansa dataframe
#        if q == 0: # if you are in the very first item
#            StarkSE = str(NewSE) # transcript_instanceust sets StarkSE as the NewSE
#            StarkI = str(Sansa['item'].iloc[q]) # transcript_instanceust sets the StarkI as the item in Sansa
#        else: # if it's not the very first item
#            StarkSE = str(StarkSE)+","+str(NewSE) # adds to old SE the new one
#            StarkI = str(StarkI)+","+str(Sansa['item'].iloc[q]) # adds current item to old one
#    TranscriptData['Starts-Ends'] = StarkSE # sets the column Start-End as StarkSE
#    TranscriptData['ExonIntronSeq'] = StarkI # sets the column ExonIntronSeq as StarkI
#    TranscriptData['Flags'].iloc[0]=flag # add flags to hash
    # make PrintingHash EIitem with Qname, Tname, and flags
#    FinalPrint = FinalPrint.append([TranscriptData], ignore_index=True) # add new item to end of hash

# print everything to output
outputz.write("Transcript\tGene\tExonIntronSeq\tUniqID\tTranscriptSize\tQueryStarts-Ends\tDBStarts-Ends\tFlags\tSequence\n")# open output and print header
#FinalPrint.to_string(outputz, header=True, index=False)
for i in range(len(FinalPrint)): # for each item in the FinalPrint hash
    outputz.write(str(FinalPrint['Tname'].iloc[i])+"\t"+str(FinalPrint['Gene'].iloc[i])+"\t"+str(FinalPrint['ExonIntronSeq'].iloc[i])+"\t"+str(FinalPrint['Starts-Ends'].iloc[i])+"\t"+str(FinalPrint['Flags'].iloc[i])+"\n") # print database to output

# write errors and everything to log:
# print number of errors, number of reads, number of flags reported, and flags itself to log
log.write("\n\n") # creates space between 

# close every used file
#outputz.close()# close output
log.close() # closes log
fastaz.close() # closes fasta file
#inputz.close() # closes blat file
# end
