#!bin/usr/python3
import sys, argparse, os
import pandas as pd
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


# open output and print header
outputz.write("Transcript\tGene\tExonIntronSeq\tFlags\n")

# open log and print timestamp, input name, and output name.
log.write("\n\n#########################\nNew usage of table_creator.py at " + str(datetime.now()) + ".\n The input used was " + str(inputz.name) + ", and the output was: " + str(outputz.name) + ".\n")

# read input into a dataframe:
inputz.close()
inputz = pd.read_csv(args.blat, sep='\t', header=None)

# get uniq transcripts from input[:,9] -> i.e. 10th column
UniqTranscripts = inputz[9].unique()
ToPrint = pd.DataFrame()#columns=['match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'Tname', 'Tsize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts', 'Gene', 'Items', 'Flags'])

# for each uniq transcript:
for i in UniqTranscripts:
    flag = ""
    NewHash = pd.DataFrame()
    # get all apearances of it in input
    temp = inputz[inputz[9] == i]
    temp[21] = "NA"
    temp[22] = "NA"
    # for each instace:
    for j in range(len(temp)):
        # get Qstart [11], Qend [12], Tname [13]
        # check if it's an intron:
        if "intron" in temp[13][j]:
            log.write("\t Error: INTRON alert. "+temp[13][j]+"is an intron.\n")
            Part1, Part2, NewItemB = temp[13][j].split(":")
            NewItemA, Gene3 = Part2.split("_")
            NewItem = NewItemA+"_"+NewItemB
            Gene1, MehIntron, Gene2 = Part1.split("_")
            if ((Gene1 != Gene2) or (Gene1 != Gene3) or (Gene2 != Gene3)):
                log.write("\t\t Error: Intron between different genes in "+temp[13][j]+"!!!\n")
                if flag == "":
                    flag = "z"
                else:
                    flag = flag+", z"
            else:
                if flag == "":
                    flag = "w"
                else:
                    flag = flag+", w"
        # parse name/genes
        else:
            NewGenes, NewItem = temp[13][j].split(":")
            Gene1, Gene2 = NewGenes.split("_")
            if Gene1 != Gene2:
                log.write("\t Error: Exon of two different genes in "+temp[13][j]+"!!!\n")
                if flag == "":
                    flag = "y"
                else:
                    flag = flag+", y"
        temp[21][j] = Gene1
        temp[22][j] = NewItem
        # if Qstart > Qend
        if (temp[11][j] > temp[12][j]):
            problematic1 = temp[11][j]
            problematic2 = temp[12][j]
            temp[11][j] = problematic2
            temp[12][j] = problematic1
            log.write("\t Error: "+temp[13][j]+" had start bigger than end.\n")
            if flag == "":
                flag = "a"
            else:
                flag = flag+", a"
            # Qstart and Qend are switched
        # for item in InstanceHash.Tname:
        for k in range(len(NewHash)):
            #HashGene = NewHash[13][k].split("_")
            # if new Tname != InstanceHash[item].Tname:
            if (temp[21][j] != NewHash[21][k]):#Gene1 != HashGene[0]):
                log.write("\t Error: "+temp[13][j]+" and "+NewHash[13][k]+" are from different genes.\n")
                # log error
                # print both Tnames to log
                if flag == "":
                    flag = "x"
                else:
                    flag = flag+", x"
                # add flag
            # possibiblities where new is inside old sequences:
            if (((temp[11][j] > NewHash[11][k]) and (temp[12][j] <= NewHash[12][k])) or ((temp[11][j] == NewHash[11][k] ) and (temp[12][j] < NewHash[12][k]))):
                # write error to log
                log.write("\t Error: "+temp[13][j]+" is contained inside "+NewHash[13][k]+".\n")
                # add flag
                if flag == "":
                    flag = "b"
                else:
                    flag = flag+", b"
            # when sequences start and end in the same places:
            elif ((temp[11][j] == NewHash[11][k]) and (temp[12][j] == NewHash[12][k])):
                # write error to log:
                log.write("\t Error: "+temp[13][j]+" and "+NewHash[13][k]+" are probably the same.\n")
                # add flag
                if flag == "":
                    flag = "c"
                else:
                    flag = flag+", c"
            # when new is partially inside old:
            elif (((temp[11][j] < NewHash[11][k]) and ((temp[12][j] < NewHash[12][k]) and (temp[12][j] > NewHash[11][k]))) or ((temp[12][j] > NewHash[12][k]) and ((temp[11][j] > NewHash[11][k]) and (temp[11][j] < NewHash[12][k])))):
                # write error to log:
                log.write("\t Error: "+temp[13][j]+" is partially inside "+NewHash[13][k]+".\n")
                # add flag
                if flag == "":
                    flag = "d"
                else:
                    flag = flag+", d"
            # when old is inside new
            elif (((temp[11][j] == NewHash[11][k]) and (temp[12][j] > NewHash[12][k])) or ((temp[11][j] < NewHash[11][k]) and (temp[12][j] >= NewHash[12][k]))):
                # write error to log:
                log.write("\t Error: "+temp[13][j]+" contains "+NewHash[13][k]+".\n")
                # add flag
                if flag == "":
                    flag = "e"
                else:
                    flag = flag+", e"
        # add new instance to InstanceHash
        NewHash = pd.concat([NewHash, pd.DataFrame(temp.loc[[j]])])
    # sort InstanceHash according to Qend
    # sort InstanceHash according to Qstart
    NewHash.sort_values(by=[11,12], inplace=True)
    NewHash[23]=flag
    # make PrintingHash NewItem with Qname, Tname, and flags
    # for item in InstanceHash:
    ToPrint = pd.concat([ToPrint, pd.DataFrame(NewHash.loc[[0]])])
    ToPrint[22][len(ToPrint)-1] = ""
    for i in range(len(NewHash)):
        if ToPrint[22][len(ToPrint)-1] == "":
            ToPrint[22][len(ToPrint)-1] = NewHash[22][i]
        else:
            ToPrint[22][len(ToPrint)-1] = ToPrint[22][len(ToPrint)-1]+","+NewHash[22][i]
        # PrintingHash[NewItem].EIList = PrintingHash[NewItem].EIList + InstanceHash[item].ExonIntron
# print PrintingHash to output
FinalPrint = ToPrint.loc[:,[9,21,22,23]]#rint[9],ToPrint[21],ToPrint[22],[ToPrint[23]],[ToPrint[9]+ToPrint[21]+ToPrint[22]])
FinalPrint.to_string(outputz, header=False, index=False)
#for i in range(len(ToPrint)):
#    outputz.write(ToPrint.loc[[i]])
# close output
outputz.close()
# print number of errors, number of reads, number of flags reported, and flags itself to log
# close log
log.close()
# end
