#!/bin/bash
end_task=18850
task=18649

while [ $task -le $end_task ]
	do 
		qdel $task
		let task=task+1
		done
