#!/bin/bash
#
#we first start by giving the cluster a few options on the job: which queue to put it into (nick), and the name we are giving it
#SBATCH --partition=defaultp
#SBATCH --job-name=AHHHH
#SBATCH --output=AHHH_output
#
#Number of CPU cores to use within one node
#SBATCH -c 1
#
#Define the number of hours the job should run. 
#Maximum runtime is limited to 10 days, ie. 240 hours
#SBATCH --time=10:00:00
#
#Define the amount of RAM used by your job in GigaBytes
#In shared memory applications this is shared among multiple CPUs
#SBATCH --mem=10G
#
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

#run commands on SLURM's srun

srun --cpu_bind=verbose
