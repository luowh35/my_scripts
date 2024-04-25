#!/bin/bash




for ((i=0; i<=9; i++)); 

do  
	for ((j=0; j<=9; j++))
		do
	cd task.000.0000$i$j; 
	mlp convert --input_format=outcar OUTCAR ./$i$j.cfg
	cat $i$j.cfg >> ../init.cfg
	cd ..
	done
done

for ((i=0; i<=9; i++)); 

do  
	for ((j=0; j<=9; j++))
		do
	cd task.001.0000$i$j; 
	mlp convert --input_format=outcar OUTCAR ./$i$j.cfg
	cat $i$j.cfg >> ../init.cfg
	cd ..
	done
done
