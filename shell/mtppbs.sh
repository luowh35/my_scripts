#!/bin/bash
#PBS -N Cu_mtp
#PBS -l nodes=1:ncpus=64
#PBS -j n
##PBS -q workq
#PBS -q fastq
#PBS -e ${PBS_JOBNAME}.err
#PBS -o ${PBS_JOBNAME}.out

export OMP_NUM_THREADS=1
cd $PBS_O_WORKDIR
TMP_DIR=./out
mpirun -np 64 mlp train init.almtp train.cfg --save_to=./pot.almtp  >log.out
#../mlp check_errors ./out/pot.almtp test.cfg --log=stdout --report_to=$TMP_DIR/errors.txt
#../mlp calculate_efs pot.almtp train.cfg --output_filename=$TMP_DIR/calculated.cfg
