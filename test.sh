#!/bin/bash
#
#we first start by giving the cluster a few options on the job: which queue to put it into (nick), and the name we are giving it
#SBATCH --partition=bigmem
#SBATCH --job-name=BlatingGonadsHeins
#SBATCH --output=blatgonadsHeins.output
#
#Number of CPU cores to use within one node
#SBATCH -c 5
#
#Define the number of hours the job should run. 
#Maximum runtime is limited to 10 days, ie. 240 hours
#SBATCH --time=240:00:00
#
#Define the amount of RAM used by your job in GigaBytes
#In shared memory applications this is shared among multiple CPUs
#SBATCH --mem=50G
#Send emails when a job starts, it is finished or it exits
#SBATCH --mail-user=jraices@ist.ac.at
#SBATCH --mail-type=ALL
#
#Do not requeue the job in the case it fails.
#SBATCH --no-requeue
#
#Do not export the local environment to the compute nodes
#SBATCH --export=NONE
unset SLURM_EXPORT_ENV
#
#Set the number of threads to the SLURM internal variable
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
#
#load any module you need here
module load blat
module load samtools

#run commands on SLURM's srun
# runs blat comparing two samples, the Query -q is RNA and the Databas
srun --cpu_bind=verbose blat -t=dna -q=rna -minScore=80 /nfs/scistore03/vicosgrp/jraices/melanogaster/FlyBase_Sxl_exons.fasta /nfs/scistore03/vicosgrp/jraices/melanogaster/FlyBase_Sxl_extended.fasta test.blat
#first let's make sure that each transcript only maps to a single reference gene
srun --cpu_bind=verbose awk '{if($1 ~ /^[0-9]/) print $0}' test.blat >test_noheader.blat

srun --cpu_bind=verbose sort -k 10 test_noheader.blat >test.blat.sorted

srun --cpu_bind=verbose perl ~/programs/2-julia_redremov_blat.pl test.blat.sorted


