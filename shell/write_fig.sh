#!/bin/bash

read -t 30 -p "input the log number?" num


for ((i=0; i<=num; i+=10))
	do     
		cat $i.lammpstrj >> lmp.trj
	done
