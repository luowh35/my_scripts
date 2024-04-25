#!/bin/bash
for((i=2;i<=10;i++))
	do
		mkdir $i'dir'
		sed -i '4c '$i' '$i' '$i'' KPOINTS
		cp INCAR POSCAR KPOINTS POTCAR pbs.sh $i'dir'
		cd $i'dir'
		qsub pbs.sh
		cd ../
	done
