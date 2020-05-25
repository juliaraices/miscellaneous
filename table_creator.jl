# Julia Raices
# November 2019
# Program to create tables with exon/intron data from blat output

using CSV
using DataFrames
using Dates

given1=""
given2=""

given1 = ARGS[1] #reads the first argument after program call
#given1 = "test.out"
#given1="dmel_analysis/whole_body/isoseq/both_sexes_mixed/transcripts/both_exonintron.blat.final"
given2 = ARGS[2] #reads the 2nd argument after the program call
#given2 = "testandoJL.out"

if isempty(given1) | isempty(given2) | (given1==given2)
	print("ERROR: the given files are not usable\n")
	exit()
end

trans = CSV.read(given1, delim="\t", header=true) # opens the first argument as a tsv table
outputz=open(given2, "w") #opens the 2nd argument to write on it (it's the output
log=open("maketablesJL.log", "w") #also opens a log so that any errors os stuff can be recorded
#oooo=open("meow.test", "w")

print(outputz, "#Flags meaning: 1 - Intron between genes\n\t# 2 - transcript has parts starting or ending inside one another\n\t# 3 - transcript has more than one reference\n\t# 4 - transcript error (different transcripts treated as the same\ngene\ttranscript\texon_intron\tuniqID\tflags\n")
# first prints header and information on the output
print(log, "\n\n", Dates.now(),"\n") #writes the date and time on the log

unique_trans=unique(trans[:10]) #selects the 10th column of the blat file and gets all the names that appear in it, creating a new list with those unique names
#length(unique_trans) #amount of unique reads/transcripts
# set the counters to 0
toout=0
intrs=0
Wintrs=0
Nintrs=0
exns=0
# make a dataframe to store the data for the transcripts
list=DataFrame(transc=String[], times=Int64[], gene=String[], exons=String[], flags=String[])

# for every transcript in the unique list
for k in 1:length(unique_trans)
	temp=trans[occursin.(unique_trans[k], trans[:10]), :] # create a temporary file with all instances of that transcript, and only that transcript
	temp2=sort!(sort!(temp, :13), :12) # sort the temporary file accordinf to the end and beggining of the transcript (in the reference gene)
	#set future variables to null
	exon=""
	temp2.transcripts=repeat("",length(temp2[:,:1]))
	gene_toprint = ""
	transc_toprint = ""
	flagging=""
	q=0
	#for every match in our sorted temporary file
	for i in 1:length(temp2[:,:1])
		if occursin("intron", temp2[i,:14])
		# if the match is to an intron, split it and make sure to only have the exons between which the intron is to put on  the final table
			meh, intronPA, intronPB = split(temp2[i,:14], "_")
			genePA, exonPA=split(intronPA, ":")
			genePB, exonPB=split(intronPB, ":")
			if (genePA != genePB)
				#if the intron is between different genes, mark it as an error in the log, and add a flag to the output
				print(log, "ERROR: there's an intron between genes ", genePA, " and ", genePB, "\n")
				if flagging==""
					#if there's no flag, add this one only
					flagging='1'
				else
					#if there's a flag, add this one with a separator between it and the previous flag
					flagging=flagging*'_'*'1'
				end
				temp2[i,:22] = genePA*'_'*genePB
				#since the intron is between two genes, add both to the gene parameter
				temp2[i,:14] = exonPA*'_'*exonPB
				# add the number of the exons between which the intron is
				global Wintrs=Wintrs+1 #increase counter
			else
				temp2[i,:22] = genePA
				#since the intron is within a gene, add it to the gene parameter
				temp2[i,:14] = exonPA*'_'*exonPB
				# add number of exons between which the intron is
				global Nintrs=Nintrs+1 #increase counter
			end
			global intrs=intrs+1 #increase counter
		else
			#if the match is not to an intron, is to an exon, and then we just add the gene and exon to its parameters
			temp2[i,:22], temp2[i,:14] = split(temp2[i,:14], ":")
			global exns=exns+1
		end
		#make new temporary file with everyline except the one we are looking at (so we can compare the one we are looking at to the others)
		temp3 = temp2[setdiff(1:end, i), :]
		for j in 1:length(temp3[:1])
			# for every line in the new temporary file
			if temp2[i, :12] in collect(temp3[j,:12]:temp3[j,:13]) || temp2[i, :13] in collect(temp3[j,:12]:temp3[j,:13])
				# if the start or the end of the match we are looking at is between the start and end of the line we are comparing it to print an error to the log, and flag the read
				print(log, "ERROR: transcript ", unique_trans[k], " has parts starting or ending inside one another.\n")
				if flagging==""
					#if there's no flag, add this one only
					flagging='2'
				else
					#if there's a flag, add this one with a separator between it and the previous flag
					flagging=flagging*'_'*'2'
				end
			end
			if temp2[i, :22] != temp3[j, :22]
				# if the gene is not the same between two of the matches flag it and add an error note to the log
				print(log, "ERROR: transcript ", unique_trans[k], " has more than one reference gene (", temp2[i, :22], " and ", temp3[j, :22], " )!\n")
				if flagging==""
					#if there's no flag, add this one only
					flagging="3"
				else
					#if there's a flag, add this one with a separator between it and the previous flag
					flagging=flagging*'_'*"3"
				end
				q=q+1
			end
		end

		if exon==""
			#if this is the first exon to be added to this transcript, add it to the variable
			exon=temp2[i,:14]
		else
			# otherwise add it with a comma between the previous and the new numbers
			exon=(exon*','*temp2[i, :14])
		end

		if gene_toprint==""
			#if it's the first time we are giving the transcript a reference gene, just do it
			gene_toprint = temp2[i, :22]
		elseif gene_toprint!=temp2[i,:22]
			# if we have a reference gene stablished, but this match has a different one, we add it to the previous with a spacer (in this case a pipe), and add an error to the log, and flag the transcript
			print(log, "ERROR: transcript ", unique_trans[k], " has more than one reference gene (", temp2[i, :22], " and ", gene_toprint, " )!\n")
			if flagging==""
				#if there's no flag, add this one only
				flagging="3"
			else
			#if there's a flag, add this one with a separator between it and the previous flag
				flagging=flagging*'_'*"3"
			end
			gene_toprint=gene_toprint*'|'*temp2[i,:22]
		else
			# if we have a reference gene stored and it's the same as the one now, just keep it, bc everything is fine
		end

		if transc_toprint==""
			# check if the transcript was in fact the same
			# if it is, everything is fine, if it's empty, make it that transcript
			transc_toprint = temp2[i, :10]
		elseif transc_toprint != temp2[i,:10]
			# if it's different, make an error note and add a flag
			transc_toprint = transc_toprint*"|"*temp2[i,:10]
			print(log, "ERROR: more than one transcript being analysed together! (", transc_toprint, " and ", temp2[i, :10], ")\n")
			if flagging==""
				#if there's no flag, add this one only
				flagging="4"
			else
			#if there's a flag, add this one with a separator between it and the previous flag
				flagging=flagging*'_'*"4"
			end
		end
	end
	# add this transcript to the dataframe we made for it:	
	push!(list, (gene=gene_toprint, transc=transc_toprint, exons=exon, times=length(temp2[:1]), flags=flagging))
	global toout=toout+1 # increase counter
end

#toout
#intrs
#Wintrs
#Nintrs
#exns

#if length(unique_trans)==length(list[:,1])
#	print("YES!!!")
#else
#	print("FUUUUUCK!!!!!!")
#end

#length(unique_trans)
#length(list[:,1])

print(outputz, list)

print(log, "\tThere were ", length(trans[:10]), " lines in the Transcript Table and ", toout, " of them were printed in the output. \n\t\tFrom ", intrs, " introns, ", Wintrs, " were weird introns (belonging to two different genes) and ", Nintrs, " lines corresponded to normal introns.\n")

close(outputz)
close(log)


