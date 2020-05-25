#Pkg.add("Statistics")
using Statistics
#Pkg.add("CSV")
using CSV #necessary
#Pkg.add("DataStructures")
using DataStructures #necessary
#Pkg.add("DataFrames")
using DataFrames #necesssary
using Plots #necessary
#Pkg.add("Plotly")
#using Plotly 
using Colors
#using Gadfly
using KernelDensity
using StatsPlots #necessary
pyplot(fmt=:png)

#Plots.scalefontsizes(2)

# Let's get our functions together!!! \o/

function qualiPACBio(x)
# this is a small function, that I am now trying to make into a function, here is what is does
	f = open(x)
	linecounter = 0
	siz = 0
	sizes = Int64[]
	endAs = Float64[]
	begTs = Float64[]
	midAs = Float64[]
	midTs = Float64[]
	midbigTs = Float64[]
	midbigAs = Float64[]
	sequence = ""
	for l in eachline(f) # it reads line by line
		linecounter += 1 # for each line it increases the line counters
		if occursin(">", l) # if the line has a ">", it means it's the identifier line, so we will add all data from the other line, and re-set the counters and things =]
			if linecounter > 1
				push!(sizes, siz) # then we add this new value to the array of sizes
				if siz > 100 # if the size of this read is bigger than 100 base pairs (bps)
					push!(endAs,(length(collect(eachmatch(r"A", sequence[end-99:end])))/100)) # check how many As in the last 100 bps
					push!(begTs,(length(collect(eachmatch(r"T", sequence[1:100])))/100)) # and how many Ts at the first 100 bps
					# and add those values to their respective arrays
					meh = div(siz,2) # first get the sup of half the size of the read
					#(because if you use exactly 1/2 it can have decimal numbers, and that doesn't work)
					if meh==50
						# if meh is 50 there will be issues with the allocation, so we add one, otherwise, things are fine =]
						meh +=1
					end
					push!(midAs,(length(collect(eachmatch(r"A", sequence[meh-50:meh+49])))/100)) # check how many As in the middle 100 bps
					push!(midTs,(length(collect(eachmatch(r"T", sequence[meh-50:meh+49])))/100)) # and how many Ts at the middle 100 bps
					push!(midbigTs,(length(collect(eachmatch(r"T", sequence[meh-50:meh+49])))/100))
					push!(midbigAs,(length(collect(eachmatch(r"A", sequence[meh-50:meh+49])))/100))
				else # if the read is smaller (or exactly) 100 base pairs, we:
					meh = div(siz,2) # first get the sup of half the size of the read
					#(because if you use exactly 1/2 it can have decimal numbers, and that doesn't work)
					push!(endAs,(length(collect(eachmatch(r"A", sequence[(end-meh):end])))/meh)) # than check how many As in the last halfs
					push!(begTs,(length(collect(eachmatch(r"T", sequence[1:meh])))/meh)) # and how many Ts in the first half
					push!(midAs,(length(collect(eachmatch(r"A", sequence[1:siz])))/siz)) # check how many As in the whole read
					push!(midTs,(length(collect(eachmatch(r"T", sequence[1:siz])))/siz)) # and how many Ts at the whole read
				end
				siz = 0
				sequence=""
			end
		else # if the line doesn't have a >, it has the dna/rna sequence
			siz += length(l) # first we get how long is the line, i.e. how many characters does
			sequence = string(sequence, l)
		end
	end
	return (linecounter, sizes, endAs, begTs, midAs, midTs, midbigTs, midbigAs) # returns all the arrays you want
end

function stranding(x)
	PC_strand = DataFrame(strand=[], count=[])
	# creates a new table, where we store the amount of each strand
	for tuple in counter(x[:9]) # for each pair strand/count
	    temp = DataFrame(strand=tuple[1], count=(tuple[2]/length(x[:9])))
	    # add them to this new temporary dataframe
	    append!(PC_strand, temp) # and append the 
	    # temporary dataframe to our final one
	end
	return(PC_strand)
end

function counts_fpkm(y, exp, column)
	PC_reads = DataFrame(geneFB=[], geneCG=[], reads=[], fpkm=[])
	# creates two new table, where we store the amount of reads for each gene and the amount of reads and fpkm
	if exp==""
		exp=DataFrame(gene_name=[])
		exp[column]=[]
	end
	for tuple in counter(y[:14]) # for each pair gene/reads
		# get FPKM expression from expression table
		# get it for 5 day old flies (because that's how old our flies were)
		fspkms=[]
		CG=[]
		#a=1
#		a=findall.(x->x=tuple[1], exp[:Column2])
		#a=occursin.(tuple[1],skipmissing(exp[:Column2]))
#		fspkms=exp[a, column]
		fspkms=exp[occursin.(tuple[1],exp[:Column2]), column]
		CG=exp[occursin.(tuple[1],exp[:Column2]), :Column1]
		if fspkms==[]
			fspkms=missing
			#fspkms=""
		end
		if CG==[]
			CG=missing
		end
		temp=DataFrame(geneFB=tuple[1], geneCG=CG, reads=tuple[2], fpkm=fspkms)
		#temp=DataFrame(geneFB=tuple[1], geneCB="-", reads=tuple[2], fpkm=fspkms)
		append!(PC_reads, temp) # actrually add the reads to the read dataframe
	end
	# this two dataframes is to be able to do plots easily with it all
	return(PC_reads)
end

function completing(all, PC_reads)
	for gene in all
		if gene in PC_reads[:gene]
		else
			temp = DataFrame(gene=gene, reads=0)
			append!(PC_reads, temp)
		end
	end
end

################################################# Plots #################################################

function Mdensities4(w,x,y,z,titlez,labelz,cds, titlefig, )
# gets the density for the sizes of reads in the minion data, and compares it with the sizes of
# transcripts, genes, cds..
	#pyplot()
	density([log10.(w), log10.(x), log10.(y), log10.(z)],
		xlabel="log10(size)", ylabel="density", title=titlez, alpha = 0.5, fill=0,
		color=[:LightGreen :Fuchsia :RoyalBlue :Orange],
		label=labelz, size=(1000,700))
	plot!([median(log10.(x)), median(log10.(y)), median(log10.(w)), median(log10.(z))], 
	      seriestype="vline", color=["Fuchsia", "RoyalBlue", "LightGreen", "Orange"], legend=false)
	#plot!([median(log10.(x))], seriestype="vline", color=["Fuchsia"])
	plot!([median(log10.(cds))], seriestype="vline", label="Median CDS", color=[:Lime])
	#label(["curve1", "curve 2"], "northwest")
	savefig(titlefig)
	return
end

#function Mdensities3(x,y,z,titlez,labelz,cds,titlefig)
# gets the density for the sizes of reads in the minion data, and compares it with the sizes of
# transcripts, genes, cds..
#	density([log10.(x), log10.(y), log10.(z)],
#		xlabel="log10(size)", ylabel="density", title=titlez, alpha = 0.5, fill=0,
#		color=[:Fuchsia :RoyalBlue :Orange],
#		label=labelz, size=(1000,700))
#	plot!([median(log10.(x)), median(log10.(y)), median(log10.(z))], seriestype = "vline", 
#	      color=[:Fuchsia :RoyalBlue :Orange], legend=false)
#	plot!([median(log10.(cds))], seriestype = :vline, label="Median CDS", color=[:Lime])
	
#	savefig(titlefig)
#	return
#end

function Mhists(x,w,titlez,titlefig)
	plot(layout=(2),
	histogram(Any[x], yaxis="# of reads", xaxis="%A in the end", title=titlez,
		fillcolor=[:DarkBlue], line=(0.1,0.1), fill = 0, alpha = 0.5,
		legend=false),
	histogram(Any[w], yaxis="# of reads", xaxis="%T in the beggining", title=titlez,
		fillcolor=[:LightBlue], line=(0.1,0.1), fill = 0, alpha = 0.5,
		legend=false))
# Plots histograms with the amount of A and T in the polyA tails for the minion data (with poretools and albacore)
# for males and females
	savefig(titlefig)
	return
end

function linreg(x, y)
	final = hcat(fill!(similar(x), 1), x) \ y
	return final
end
	
function Mexp(PC_given, titlez, titlefig)
	PC_counts=PC_given[completecases(PC_given),:]
	a, b = linreg(log10.(PC_counts[:fpkm].+0.000001), log10.(PC_counts[:reads].+0.000001))
	x=(minimum(log10.(PC_counts[:fpkm].+0.000001)):maximum(log10.(PC_counts[:reads].+0.000001)))
	#x=(0:1)
	scatter(log10.(PC_counts[:fpkm].+0.000001), log10.(PC_counts[:reads].+0.000001), color=[:Purple],
		size=(1000,1000), xlabel="log10(FPKM+0.000001)", ylabel="log10(Reads+0.000001)",
		title=titlez, tickfont=font(24),guidefont=font(22), legend=false)
	plot!(x, a.+b.*x, color=[:Red], legend=false)

	savefig(titlefig)
	return
end

function Mmatches(PC, titlez,titlefig)
# plots the number of reads with each match percentage value for male and female reads separatly
# (since there's a huge diference in the amount of reads in each
	histogram(Any[PC[:22]], yaxis="# of reads", xaxis="(match/(match+mismatch))", 
		fillcolor=[:RoyalBlue],
        	tickfont=font(18),guidefont=font(18), title=titlez,
	        line=(0.1,0.1), fill = 0, alpha = 0.5, legend=false)
	vline!([median(PC[:22])], seriestype = :vline, color=[:Blue],label="")

	savefig(titlefig)
	return
end

function Mgenes(PC_reads, titlez, titlefig)
# how many reads per gene, for female reads
	maxx=maximum(PC_reads[:reads])
	a=histogram(Any[PC_reads[:reads]], ylabel="# of genes", xlabel="# of reads", 
		title=titlez, fillcolor=[:HotPink],
		line=(0.1,0.1), fill = 0, alpha = 0.5,
		bins=[-1,1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,maxx],
		xlim=(-1,110), legend=false, size=(800,600))
	#### how many reads per gene, for female reads
	b=histogram(Any[PC_reads[:reads]], ylabel="# of genes", xlabel="# of reads", 
		fillcolor=[:HotPink],
		line=(0.1,0.1), legend=false, fill = 0, alpha = 0.5,
		bins=[-1,1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,maxx],
		xlim=(-1,20), ylim=(0,700))
	plot(a,b,layout=(1,2),legend=false)
	
	savefig(titlefig)
	return
end

