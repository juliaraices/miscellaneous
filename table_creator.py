#!bin/usr/python3
# import packages we will need to work with dataframes and all
import sys, argparse, os
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from datetime import datetime

# Read arguments (file names)
parser = argparse.ArgumentParser(description='Program to create a table with the list of introns/exons that comprise different reads.')
parser.add_argument("--blat", required=True, type=str, help='Output from blat of reads against introns and exons')
parser.add_argument("--output", default="IntronExonTable.output", help="Desired name for the output file. Default is IntronExonTable.output", type=str)
parser.add_argument("--log", default="TableMaker.log", help="Desired name for the log file. Default is TableMaker.log", type=str)

args = parser.parse_args()

try:
    log = open(args.log, "a") # "a" will append to the end of the file
    # open input
    inputz = open(args.blat, "r") # opens file as read only
    outputz = open(args.output, "w") # "w" will overwrite file
# If files do not open:
except FileNotFoundError or IOError:
    # report to log
    log.write("One or more of the files given was not available.\n")
    print("File name is not valid. Please try again.")
    # exit program with erros
    sys.exit("Files are not valid.")

inputz.close() # close input to prevent naming errors

# open output and print header
outputz.write("Transcript\tGene\tExonIntronSeq\tStarts-Ends\tFlags\n")

# open log and print timestamp, input name, and output name.
log.write("\n\n#########################\nNew usage of table_creator.py at " + str(datetime.now()) + ".\n\t The input used was " + str(inputz.name) + ", the output was: " + str(outputz.name) + ", and the log file is " + str(log.name) + ".\n")

# read input into a dataframe:
inputz = pd.read_csv(args.blat, sep='\t', header=None)
# give columns names to make life easier
#columns=['0.match', '1.mismatch', '2.RepMatch', '3.Ns', '4.QGapCount', '5.QGapBases', '6.TGapCount', '7.TGapBases', '8.strand', '9.Qname[exon/intron]', '10.Qsize', '11.Qstart', '12.Qend', '13.Tname[read]', '14.Tsize', '15.Tstart', '16.Tend', '17.BlockCount', '18.BlockSizes', '19.qStarts', '20.tStarts', '21.Gene', '22.ExonIntronSeq', '23.Flags'])
inputz.columns = ['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'Tname', 'Tsize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts']# to add: '21.Gene', '22.ExonIntronSeq', '23.Flags'
# add columns we will fill out later with a standard value (in this case, NA = Not Available)
inputz['Gene']="NA"
inputz['ExonIntronSeq']="NA"
inputz['Flags']="NA"
inputz['Starts-Ends']="NA"

# get uniq transcripts from input[:,13] -> i.e. 14th column
UniqTranscripts = inputz['Tname'].unique()
# makes a new data frame to put what will be outputed
#FinalPrint = pd.DataFrame(columns=['Tname', 'Gene', 'ExonIntronSeq', 'Starts-Ends', 'Flags'])
FinalPrint = pd.DataFrame(columns = ['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'Tname', 'Tsize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts', 'Gene', 'ExonIntronSeq', 'Starts-Ends', 'Flags']) # initiates temporary data frame for this transcript
# for each uniq transcript:
for i in UniqTranscripts:
    flag = "" # initiate an empty flag item
    NewHash = pd.DataFrame(columns = ['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'Tname', 'Tsize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts', 'Gene', 'ExonIntronSeq', 'Starts-Ends', 'Flags']) # initiates temporary data frame for this transcript
    # get all apearances of it in input
    temp = inputz[inputz['Tname'] == i] # makes a temporary variable only with the one read
    temp.sort_values(['Tstart','Tend'], inplace=True)
    # for each instace:
    for j in range(len(temp)):
        #get ext gene from other blat to check positions
        # check if it's an intron:
        if "intron" in temp['Qname'].iloc[j]:
            # if read has intron, make an error alert
            log.write("\t Error: INTRON alert. The "+temp['Tname'].iloc[j]+"has the following match, "+temp['Qname'].iloc[j]+", that is an intron.\n")
            # divide intron name, so we can see the genes and introns involoved
            Part1, Part2, NewItemB = temp['Qname'].iloc[j].split(":")
            NewItemA, Gene2 = Part2.split("_")
            NewItem = NewItemA+"_"+NewItemB
            MehIntron, Gene1 = Part1.split("_")
            if Gene1 != Gene2:
                # if any of the named genes is different from each other
                log.write("\t\t Error: Intron between different genes in "+temp['Qname'].iloc[j]+" for read"+temp['Tname'].iloc[j]+"!!!\n")
                NewGenes=Gene1+"_"+Gene2
                if flag == "": # add flag
                    flag = "z"
                elif not ("z" in flag):
                    flag = flag+",z"
            else: # add flag
                NewGenes=Gene1
                if flag == "":
                    flag = "w"
                elif not "w" in flag:
                    flag = flag+",w"
        # parse name/genes
        else: # if read has no intron ^^
            NewGenes, NewItem = temp['Qname'].iloc[j].split(":")
        if NewHash.empty: # if the new hash is empty we add things the easiest way ;)
            NewHash = NewHash.append(temp.iloc[j])
            NewHash['Gene'].iloc[0] = NewGenes
            NewHash['ExonIntronSeq'].iloc[0] = NewItem
        elif not NewGenes in NewHash['Gene'].iloc[0]: # if the new hash is not empty and the gene we found is not in the new hash gene name
            if "_" in NewGenes:
                NewGenes2 = NewGenes.split("_")
                for k in range(len(NewGenes2)):
                    if not NewGenes2[k] in NewHash['Gene'].iloc[0]:
                        NewHash['Gene'].iloc[0] = NewHash['Gene'].iloc[0]+"_"+NewGenes2[k]
            else:
                NewHash['Gene'].iloc[0] = NewHash['Gene'].iloc[0]+"_"+NewGenes
            if flag == "":
                flag = "y"
            elif not "y" in flag:
                flag = flag+",y"
            #NewHash['ExonIntronSeq'].iloc[0] = NewHash['ExonIntronSeq'].iloc[0]+","+NewItem
        #else:
            #NewHash['ExonIntronSeq'].iloc[0] = NewHash['ExonIntronSeq'].iloc[0]+","+NewItem
        # if Qstart > Qend
        if (temp['Tstart'].iloc[j] > temp['Tend'].iloc[j]):
            problematic1 = temp['Tstart'].iloc[j]
            problematic2 = temp['Tend'].iloc[j]
            temp['Tstart'].iloc[j] = problematic2
            temp['Tend'].iloc[j] = problematic1
            log.write("\t Error: "+temp['Qname'].iloc[j]+" had start bigger than end in the "+temp['Tname'].iloc[j]+".\n")
            if flag == "":
                flag = "a"
            elif not "a" in flag:
                flag = flag+",a"
            # Qstart and Qend are switched
        # possibiblities where new is inside old sequences:
        # get starts and ends of previous 
        SE = str(temp['Qstart'].iloc[j])+"-"+str(temp['Qend'].iloc[j])
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
    NewHash['Flags'].iloc[0]=flag
    # make PrintingHash NewItem with Qname, Tname, and flags
    FinalPrint = FinalPrint.append(NewHash, ignore_index=True)
#FinalPrint.to_string(outputz, header=True, index=False)
for i in range(len(FinalPrint)):
    outputz.write(str(FinalPrint['Tname'].iloc[i])+"\t"+str(FinalPrint['Gene'].iloc[i])+"\t"+str(FinalPrint['ExonIntronSeq'].iloc[i])+"\t"+str(FinalPrint['Starts-Ends'].iloc[i])+"\t"+str(FinalPrint['Flags'].iloc[i])+"\n")
# close output
outputz.close()
# print number of errors, number of reads, number of flags reported, and flags itself to log
log.write("\n\n")
# close log
log.close()
# end
