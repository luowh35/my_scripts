#!/bin/bash
#PBS -N vasp
#PBS -l nodes=1:ncpus=16
#PBS -j n
#PBS -e ${PBS_JOBNAME}.err
#PBS -o ${PBS_JOBNAME}.out
cd $PBS_O_WORKDIR
NP=`cat $PBS_NODEFILE|wc -l`
EXEC=/opt/ohpc/pub/apps/vasp.5.4.4/bin/vasp_std
#./record.sh
mpirun -np 48 -machinefile $PBS_NODEFILE $EXEC > log.out
