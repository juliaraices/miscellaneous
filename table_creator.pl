# April 2019
# Julia Raices
# Program to take output from blat with exons and intronsdo everything I ever did with this tables
#!/usr/bin/perl

use strict; # doesn't let you use variables without declaring them

# declared variables:
my ($i, $k, $n, $j, $l, $trans, $outname, $line, $key, $thing); # counters and strings
my (@reads, @transcript, @sorted, @exons, @temp, @temp2, @temp3, @genez, @list, @f); # arrays with raw data
my (%values); # hashs with printable data

# undefine variables, so that they don't - by chance - start not empty
undef $i;
undef $j;
undef $l;
undef $k;
undef $n;
undef @sorted;
undef @genez;
undef $thing;
undef $trans;
undef $line;
undef $key;
undef $outname;
undef @reads;
undef @list;
undef @f;
undef @transcript;
undef @exons;
undef @temp;
undef @temp2;
undef @temp3;
undef %values;

$j = 0;

# sees what is the argument (after the program was called) and stores it. It should be the name of file to be used by the program
for($i=0; $i<=$#ARGV; $i+=2){
	if($ARGV[$i] eq "-trans"){
		$trans=$ARGV[$i+1];
	}
}
for($i=0; $i<=$#ARGV; $i+=2){
	if($ARGV[$i] eq "-out"){
		$outname=$ARGV[$i+1];
	}
}

# check if files have been designated correctly, if they are not, it tells you how to use the program and exits
if($trans eq "" | $outname eq ""){
	print STDERR "Program usage: perl table_creator.pl -trans BLAT_OUTPUT_TRANSCRIPTS -out OUTPUT_NAME\n\t-trans: Table with exons and introns that compose transcripts (blat output).\n\t-out: Name and location of the output file.\n";
	exit 0;
}

# open log file and adds data from this time program was run
open (LOG, ">>table.log");

print LOG "\n".(localtime)."\nTable for transcripts data: $trans\nOutput file: $outname\n";

# finds if input files actually exists and are openable, if not, prints error in log and in stderr and exists program
#unless(open(TRA, $trans) || open(OUTPUT, '>', $outname)){
#	print STDERR "Couldn't open file, please check if file exist and if you have permission to read it.\n";
#	print LOG "Error opening file.\n";
#	exit 0;
#}

system("awk '{print $10}' $trans | sort | uniq >genelist.tmp");

open(GEN, "genelist.tmp");
while(<GEN>){
	$line=$_;
	chomp $line;
	if($line=~/Symbol/){}
	else{
		$genez[$#genez+1]=$line;
		#print $line, '\n';
	}
}
close(GEN);
system("yes | rm genelist.tmp");
undef $line;

open(F,$trans);
@list=<F>;
close F;

#foreach $thing (@genez){
#	@f=grep /$thing/, @list;

	#open(TMP, '>', $thing);
	#print TMP @f;
	#@sorted = sort {(split(/\t/, $b))[11] <=> (split(/\t/, $a))[11]} @f;
	#	@sorted = sort { my @a = split /\t/, $a; my @b = split /\t/, $b; $a[11] <=> $b[11]; } @f;

	#foreach $line (@sorted){
	#print $line;
		#AQUI
		#}
		#}
undef $line;


open(OUTPUT, '>', $outname);

# open output files, and prints header in it
print OUTPUT "gene\ttranscript\texon_intron\tuniqID\n";

open(TRA, $trans);
# get transcript data from table
while(<TRA>){ # as far as there are things/lines in the file
	$line=$_; # read it line by line
	chomp $line; # remove end of line character
	@reads=split(/\t/, $line); # split line where there's a tab
	if($line=~/Symbol/){} # if line is the header, ignore it
	@transcript=split(/\//,$reads[9]); # for the 10th column (perl starts counting at 0) split it in th "/" - this is not necessary, but it will make it prettier
	if(index($reads[13], 'intron') != -1){#here we check if the match was for an intron, and if it was, we will do things a little differently, because introns have a different form of annotation
		# the annotation for introns goes as: intron_FBgn###:#_FBgn###:#
		@temp=split(/_/,$reads[13]); # this separetes the beggining of the intron from its end
		@temp2=split(/:/, $temp[1]); # this stores the 1st exon that borders the intron
		@temp3=split(/:/, $temp[2]); # and this, is the 2nd exon
		if($temp2[0]!=$temp3[0]){#to make sure that introns are contained within the name gene
			print LOG "Error: there's an intron between genes $temp2[0] and $temp3[0]\n";
			# if the intron is between different genes (what shouldn't happen) mark it on the log!
			$exons[0]="$temp2[0]_$temp3[0]";
			$exons[1]="$temp2[1]_$temp3[1]";
			$j++;
		}
		else{
			$exons[0]="$temp2[0]";
			$exons[1]="$temp2[1]_$temp3[1]";
			$l++;
		}
	}
	else{
		@exons=split(/:/,$reads[13]);
	}

	if(exists($values{$transcript[1]})){
		#if this transcript has already been found, add to it's entry
		$values{$transcript[1]}[2]="$values{$transcript[1]}[2],$exons[1]";
		if($values{$transcript[1]}[0]==$exons[0]){}
		else{
			$values{$transcript[1]}[0]="$values{$transcript[1]}[0],$exons[0]";
			print LOG "ERROR: transcript $transcript[1] has more than one reference gene!\n";
			#mark in the log if the transcript is matched to differnt genes
		}
	}
	else{#otherwise create a new entry
		$values{$transcript[1]}[0]="$exons[0]";
		$values{$transcript[1]}[1]="$transcript[1]";
		$values{$transcript[1]}[2]="$exons[1]";
	}
	$k++;

}

## prints data in output. gives an NA (Not Avaiable) for not avaiable dn/ds data.
foreach $key (keys %values){ # as a foreach was used, there are only uniq copies of each CG in the final output file.
	$n++;
	print OUTPUT "$values{$key}[0]\t$values{$key}[1]\t$values{$key}[2]\t$values{$key}[0]/$values{$key}[1]_$values{$key}[2]\n";
}

# print what was done and found in log file
print LOG "\tThere were $k lines in the Transcript Table and $n of them were printed in the output.\n\t\t$j lines had weird introns (belonging to two different genes).\n\t\t$l lines corresponded to normal introns.\n";

# close files used and exit program.
close LOG;
close OUTPUT;
close TRA;

exit;

