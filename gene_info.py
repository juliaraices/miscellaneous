#!bin/usr/python3
## import packages we will need to work with dataframes and all
import re, sys, argparse, os, csv # import packages to call commands, to parse arguments given when calling the program
from tabulate import tabulate
from Bio import SeqIO # import part of the Bio package that deals with input and output of sequences/fasta/fastq/etc
import numpy as np # imports numpy for dealing with numbers and stats
import pandas as pd # pandas is for dealing with dataframes
pd.options.mode.chained_assignment = None # default='warn' # changes the options for pandas so it doesn't give warmings for everything. in other words: I'm bad and I don't want to know about it =/
from datetime import datetime # allows us to add the date/time to the code/output

# read inputs:
# allows to create an automatic message for usage and checks if all the parameters have been provided, or give the default input for each parameter that has a default value/file
parser = argparse.ArgumentParser(description='Program to create a table that concentrates a lot of published data into one workable table.') # sets the description for the full program, in case it's called with no arguments
parser.add_argument("--ageZ", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/age_color/S1ageZhangetal2010.csv", type=str, help='Table containing age data for drosophila melanogaster. Default is S1 supplemental table from Zhang et al 2010') #
#age2 = pd.read_table("/nfs/scistore03/vicosgrp/jraices/melanogaster/age_color/S1ageZhangetal2010.csv", header=1, sep='\t') #
parser.add_argument("--age", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/age_color/AssisBachtrog2013.txt", type=str, help='Table containing age data for drosophila melanogaster. Default is S1 supplemental table from Assis and Bachtrog') #
#age = pd.read_table("/nfs/scistore03/vicosgrp/jraices/melanogaster/age_color/AssisBachtrog2013.txt", header=1, sep='\t') # for de-bugging
parser.add_argument("--chrmColourS2", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/age_color/s2.bg3s2.200bp.jkh.rm.chr3.s11.0s.reduced.merged.wig", type=str, help='Table with chromatin color1 data from Kravcchenco et al 2017 in Cell.') #sets the default chromosome colour file to be used in case it is not provided by the user
#color1 = pd.read_csv("/nfs/scistore03/vicosgrp/jraices/melanogaster/age_color/bg3.bg3s2.200bp.jkh.rm.chr3.s11.0s.reduced.merged.wig", header=2, sep='\t') #for de-bugging
parser.add_argument("--chrmColourBG3", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/age_color/bg3.bg3s2.200bp.jkh.rm.chr3.s11.0s.reduced.merged.wig", type=str, help='Table with chromatin color data from Kravcchenco et al 2017 in Cell.') #sets the default chromosome colour file to be used in case it is not provided by the user
#color2 = pd.read_csv("/nfs/scistore03/vicosgrp/jraices/melanogaster/age_color/s2.bg3s2.200bp.jkh.rm.chr3.s11.0s.reduced.merged.wig", header=2, sep='\t') #for de-bugging
parser.add_argument("--chrLoc", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/DBgeneextQei.final.blat", type=str, help='Blat output from intron+exons against a full gene/extended gene dataset. Default is the blat output for extended genesDB vs exons+introns in Drosophila melanogaster') # sets the default genome blat file to be used in case it is not provided by the user
#location = pd.read_table("/nfs/scistore03/vicosgrp/jraices/melanogaster/DBgeneextQei.final.blat", header=1, sep='\t') # for de-bugging
parser.add_argument("--rosetta", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/fbgn_annotation_ID_fb_2021_01.tsv", type=str, help='FlyBase\'s correspondencce of gene name and FBgn. Default is the from January 2021') # sets the default renompondence of FBgn to gene name from FlyBase to be used in case it is not provided by the user
#roseta = pd.read_table("/nfs/scistore03/vicosgrp/jraices/melanogaster/fbgn_annotation_ID_fb_2021_01.tsv", header=5, sep='\t') # for debugging
parser.add_argument("--map", default="/nfs/scistore03/vicosgrp/jraices/melanogaster/gene_map_table_fb_2021_02.tsv", type=str, help='FlyBase\'s location of genesDB in chromosomes. Default is the from January 2021') # sets the default renompondence of FBgn to gene name from FlyBase to be used in case it is not provided by the user
#mapa = pd.read_table("/nfs/scistore03/vicosgrp/jraices/melanogaster/gene_map_table_fb_2021_02.tsv", header=5, sep='\t') # for de-bugging
parser.add_argument("--output", default="AllThings.output", help="Desired name for the output file. Default is .output", type=str) # sets the output file name if none is given. If there's already a file with that name, it will be overwritten.
#outputz = open("AllThings.output", "w") # for de-bug
parser.add_argument("--log", default="geneinfo.log", help="Desired name for the log file. Default is .log", type=str) # sets the log file name if none is given. The new log will be appended to the end of the given file.
#log = open("geneinfo.log", "a") # for de-bug

args = parser.parse_args()

# checkif all files open
try: # makes sure you can open all the files
    log = open(args.log, "a") # "a" will append to the end of the file
    # open input
    age = pd.read_table(args.age, header=1, sep='\t')# read input into a dataframe
    age2 = pd.read_table(args.ageZ, header=1, sep='\t')# read input into a dataframe
    color2 = pd.read_csv(args.chrmColourS2, header=2, sep='\t')# read input into a dataframe
    color1 = pd.read_csv(args.chrmColourBG3, header=2, sep='\t')# read input into a dataframe
    roseta = pd.read_table(args.rosetta, header=5, sep='\t')
    mapa = pd.read_table(args.map, header=5, sep='\t')# read input into a dataframe
    location = pd.read_table(args.chrLoc, header=1, sep='\t')# read input into a dataframe
    outputz = open(args.output, "w") # "w" will overwrite file
#if files do not open:
except FileNotFoundError or IOError: # if any of the files is not openned, shuts down the program and logs the errors
    # report to log
    log.write("One or more of the files given was not available.\n") # prints error to log
    print("File name is not valid. Please try again.") # prints error to standard output
    # exit program with erros
    sys.exit("Files are not valid.") # prints error as system error and leaves the program

#write the used files and when it was started
log.write("\n\n#########################\nNew usage of gene_info.py at " + str(datetime.now()) + ".\n\t The age input used was " + str(args.age) + ", the chromatin colour input was: " + str(args.chrmColourBG3) + ", the chromosome location input was: " + str(args.chrLoc) + " and the output was: " + str(outputz.name) + ".\n") # open log and print timestamp, inputs names, and output name.

## Let's start with the easy ones XD
# age and location:
# goal: gene[1] age[2] chromosome #[2] muller element[3] location in chr[4] introns/exons[5] location introns/exons in gene[6] location introns/exons in chr[7] #chromatin color1 of introns/exons[8]

outputz.write("Gene\tChromosome\tMullerElement\tExonsIntronsSequence\tExonIntronInChromosomeLoci\tGeneSize\tExonIntronInGeneLoci\tAgeAssis\tAgeZhang\tColourBG3\tColourS2\tAge\tAgeFrom\tColour\tColourFrom\n")# open output and print header
mapa.columns=('spp','symbol','FBgn', 'recombination_loci', 'cyto_loci', 'seq_loci')
color1.columns=('chrom', 'start', 'end', 'ColorBG3Number')
color2.columns=('chrom', 'start', 'end', 'ColorS2Number')
location.columns=('match', 'mismatch', 'RepMatch', 'Ns', 'QGapCount', 'QGapBases', 'TGapCount', 'TGapBases', 'strand', 'Qname', 'Qsize', 'Qstart', 'Qend', 'GeneName', 'genesDBize', 'Tstart', 'Tend', 'BlockCount', 'BlockSizes', 'qStarts', 'tStarts') # sets the names of the columns from the blat file
age.columns=('child','parent','ancestral','DNA/RNA','Age','D(P,A)','D(C,A)','D(PC,A)', 'Class', 'Tau(C)', 'Tau(P)', 'Tau(A)', 'Tiss(C)', 'Tiss(P)', 'Tiss(A)')
age.drop(['parent','ancestral','DNA/RNA','D(P,A)','D(C,A)','D(PC,A)', 'Class', 'Tau(C)', 'Tau(P)', 'Tau(A)', 'Tiss(C)', 'Tiss(P)', 'Tiss(A)'], inplace=True, axis=1)
age2.columns=('id', 'chrom', 'branch', 'bias', 'tissue_number', 'testis_value', 'ovary_value', 'adj_pvalue')
age2.drop(['bias', 'tissue_number', 'testis_value', 'ovary_value', 'adj_pvalue'], inplace=True, axis=1)
roseta.columns=('id1', 'organism_abbreviation', 'FBgn', 'secondary_FBgn#(s)', 'id', 'secondary_annotation_ID(s)')
roseta.drop(['organism_abbreviation', 'secondary_FBgn#(s)', 'secondary_annotation_ID(s)'], inplace=True, axis=1)


genesDB = pd.DataFrame(columns=['FBgn', 'Chrm', 'Muller', 'Geneloci', 'Size', 'EIseq', 'QEIloci', 'AgeAssis', 'AgeZhang', 'ColourBG3', 'ColourS2', 'Age', 'AgeFrom', 'Colour', 'ColourFrom'])


for lineN in range(len(mapa['FBgn'])):
    if mapa['spp'].iloc[lineN] != "Dmel":
        continue
    if ":" in str(mapa['seq_loci'].iloc[lineN]):
        corFinal = 'NA'
        corFrom='NA'
        chromosome, startEnd = str(mapa['seq_loci'].iloc[lineN]).split(':')
        starts1, ends1 = str(startEnd).split('..')
        ends = re.sub("[\(\[].*?[\)\]]", "", ends1)
        starts = re.sub("[\(\[].*?[\)\]]", "", starts1)
        sizing = int(ends) - int(starts)
        if not (color1[(color1['start'] <= int(starts)) & (color1['end'] >= int(ends))].empty):
            cor1 = color1[(color1['start'] <= int(starts)) & (color1['end'] >= int(ends))]['ColorBG3Number'].iloc[0]
            corFinal = color1[(color1['start'] <= int(starts)) & (color1['end'] >= int(ends))]['ColorBG3Number'].iloc[0]
            corFrom = 'BG3'
        else:
            cor1 = 'NA'
        if not (color2[(color2['start'] <= int(starts)) & (color2['end'] >= int(ends))].empty):
            cor2 = color2[(color2['start'] <= int(starts)) & (color2['end'] >= int(ends))]['ColorS2Number'].iloc[0]
            if corFinal=='NA':
                corFinal = color2[(color2['start'] <= int(starts)) & (color2['end'] >= int(ends))]['ColorS2Number'].iloc[0]
                corFrom = 'S2'
        else:
            cor2 = 'NA'
    else:
        chromosome = 'NA'
        starts = 'NA'
        ends = 'NA'
        sizing='NA'
    if chromosome == '4':
        muller = "F"
    elif chromosome == 'X':
        muller = "A"
    elif chromosome == '2L':
        muller = "B"
    elif chromosome == '2R':
        muller = "C"
    elif chromosome == '3L':
        muller = "D"
    elif chromosome == '3R':
        muller = "E"
    elif chromosome == 'Y':
        muller = "Y"
    elif chromosome == 'NA':
        muller = 'NA'
    else:
        muller = "Other"
    newRow = {'FBgn':mapa['FBgn'].iloc[lineN], 'Chrm':chromosome, 'Muller':muller, 'GeneLoci':str(starts)+"-"+str(ends), 'Size':sizing, 'EIseq':'NA', 'QEIloci':'NA', 'AgeAssis':'NA', 'AgeZhang':'NA', 'ColourBG3':color1, 'ColourS2':color2, 'Age':'NA', 'AgeFrom':'NA', 'Colour':corFinal, 'ColourFrom':corFrom}
    genesDB = genesDB.append(newRow, ignore_index=True)

agerose = pd.merge(age2, roseta, on=["id"], how="left")

for linha in range(len(agerose['FBgn'])):
    if genesDB['FBgn'].isin([agerose['FBgn'].iloc[linha]]).any():
        genesDB.AgeZhang[genesDB['FBgn'].isin([agerose['FBgn'].iloc[linha]])] = agerose['branch'].iloc[linha]
        genesDB.Age[genesDB['FBgn'].isin([agerose['FBgn'].iloc[linha]])] = agerose['branch'].iloc[linha]
        genesDB.AgeFrom[genesDB['FBgn'].isin([agerose['FBgn'].iloc[linha]])] = "Zhang et al. 2010"

for lineS in range(len(age['child'])):
    if genesDB['FBgn'].str.contains(age['child'].iloc[lineS]).any():
        genesDB.AgeAssis[genesDB['FBgn'].str.contains(age['child'].iloc[lineS])] = age['Age'].iloc[lineS]
        genesDB.Age[genesDB['FBgn'].str.contains(age['child'].iloc[lineS])] = age['Age'].iloc[lineS]
        genesDB.AgeFrom[genesDB['FBgn'].str.contains(age['child'].iloc[lineS])] = "Assis and Bachtrog 2013"

# read blat table
# read and organize input
# give columns names to make life easier
# name columns
#columns=['0.match', '1.mismatch', '2.RepMatch', '3.Ns', '4.QGapCount', '5.QGapBases', '6.TGapCount', '7.TGapBases', '8.strand', '9.Qname[exon/intron]', '10.Qsize', '11.Qstart', '12.Qend', '13.Tname[read]', '14.Tsize', '15.Tstart', '16.Tend', '17.BlockCount', '18.BlockSizes', '19.qStarts', '20.tStarts', '21.Gene', '22.ExonIntronSeq', '23.Flags'])

# add output columns/names
# add columns we will fill out later with a standard value (in this case, NA = Not Available)
location['QueryStarts-Ends'] = 'NA' # create a new column, and sets start-end in query
location['genesDBtarts-Ends'] = 'NA' # create a new column, and sets start-ends in transcript
location['EIseq'] = 'NA' # create a new column, and sets start-ends in transcript
location['EIloci'] = 'NA' # create a new column, and sets start-ends in transcript
location['QEIloci'] = 'NA' # create a new column, and sets start-ends in transcript


for gene in location['GeneName']: # for each gene:
    EIitems = [] # starts empty hash to store the exons/introns sequence
    EIlocis = [] # starts an empty hash to store the loci (start-finish) of each match
    InputSubset = location[location['GeneName'] == gene] #subsets the full input only to the items that are from transcript transcript_name
    InputSubset.sort_values(['Tstart','Tend'], inplace=True) # sort according to Tstart first, and within that, accoridng to Tend
    for instance in range(len(InputSubset['Qname'])): # for each instance in the subset
        InputSubset['QueryStarts-Ends'].iloc[instance] = str(InputSubset['Qstart'].iloc[instance]) + '-' + str(InputSubset['Qend'].iloc[instance]) # sets start-end in query
        InputSubset['genesDBtarts-Ends'].iloc[instance] = str(InputSubset['Tstart'].iloc[instance]) + '-' + str(InputSubset['Tend'].iloc[instance]) # sets start-ends in transcript
        if not EIitems: # if there are no items in the hash
            EIitems =  InputSubset['Qname'].iloc[instance] # add the item to the sequence hash
            EIlocis =  InputSubset['genesDBtarts-Ends'].iloc[instance] # add start-end to the start-end hash
            QEIlocis =  InputSubset['QueryStarts-Ends'].iloc[instance] # add query start-end to the query start-end hash
        else: # if the hash is not empty
            EIitems =  str(EIitems) + ',' + str(InputSubset['Qname'].iloc[instance]) # concatenate the new item to the old ones
            EIlocis =  str(EIlocis) + ',' + str(InputSubset['genesDBtarts-Ends'].iloc[instance]) # same
            QEIlocis =  str(QEIlocis) + ',' + str(InputSubset['QueryStarts-Ends'].iloc[instance]) # same
    genesDB.EIseq[genesDB['FBgn'].str.contains(gene)] = EIitems
    genesDB.EIloci[genesDB['FBgn'].str.contains(gene)] = EIlocis
    genesDB.QEIloci[genesDB['FBgn'].str.contains(gene)] = QEIlocis # adds new values to dataframe

print(tabulate(genesDB, index=False), file=outputz)


# close every used file
#outputz.close()# close output
log.close() # closes log
#age.close() # closes age file
#location.close() #close chr location blat file
#color1.close() #close color1 file
# end


