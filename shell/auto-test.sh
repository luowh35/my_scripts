#!/bin/bash
path_now="$(pwd)" #current path
n=${path_now: -1} #find the number in the iter0000yx
if [ $n -ne 0 ]; then

m=$((n-=1)) #the number minus 1
l=${#path_now} #length of the path
length=$((l-=1)) #
path_cut="${path_now:0:$length}" #cut the last number of the path
path_last=${path_cut}"$m" #cd the iter0000y(x-1)
path_fp=${path_last}"/02.fp/data*"
path_pb=${path_now}"/00.train/graph.000.pb"
path_loss=${path_now}"/00.train/000/lcurve.out"
path_model_dev=${path_now}"01.model_devi"
cp -r $path_fp .  # copy the data file to current list
cp $path_pb .  # copy the pb file to current list
cp $path_loss .  # copy the loss function to the current list
n_data="$(find data* | wc -l)"
n_data=$((n_data/14))  #count the number of the data.00x
i=0
read -t 30 -p "how many data points what you want test?" num 
#dp test part
while [ $i -lt $n_data ]
	do
		dp test -m graph.000.pb -s data.00$i -n $num -d DP_DFT_00$i.out
		cat DP_DFT_00$i.f.out >> DP_DFT_f.out
		let i=i+1
		done

#RMSEtest part
cp /home/luowh35/scripts/RMSEtest.py .
python RMSEtest.py
#learn rate part
cp /home/luowh35/scripts/learn_rate.py .
python learn_rate.py
#Maxdev part
j=$((n+=2))
y=${path_now: -2:1}
k=$y$j
a=$(grep \"sys_idx\" ../param.json |sed -n $k'p')
b=${a#*temps}
c=${b%press*}
d=${c#*[}
e=${d%]*}
echo ${d%]*} > temp
s="$(grep -o "," temp |wc -l)"
r=$((s+=1))
for((i=1;i<=$r;i++))
	do
		echo $e | awk -F ',' '{print $'$i'}' >>01.model_devi/temp
		done
cp /home/luowh35/scripts/distribution_fmax.sh 01.model_devi/
cp /home/luowh35/scripts/MaxdevForce.py . 
cd 01.model_devi
. distribution_fmax.sh
rm temp
cp Max_Devi_F .. 
cd ..
python MaxdevForce.py

else #the last number is 0
y=${path_now: -2:1} #find the y in the iter0000y0
((y-=1)) # iter0000(y-1)0
m=9 # 10-1=9
l=${#path_now} #length of the path
length=$((l-=2)) #
path_cut="${path_now:0:$length}" #cut the last number of the path
path_last=${path_cut}"$y""$m" #cd the iter0000y(x-1)
path_fp=${path_last}"/02.fp/data*"
path_pb=${path_now}"/00.train/graph.000.pb"
path_loss=${path_now}"/00.train/000/lcurve.out"
path_model_dev=${path_now}"01.model_devi"
cp -r $path_fp .  # copy the data file to current list
cp $path_pb .  # copy the pb file to current list
cp $path_loss .  # copy the loss function to the current list
n_data="$(find data* | wc -l)"
n_data=$((n_data/14))  #count the number of the data.00x
i=0
read -t 30 -p "how many data points what you want test?" num 
#dp test part
while [ $i -lt $n_data ]
	do
		dp test -m graph.000.pb -s data.00$i -n $num -d DP_DFT_00$i.out
		cat DP_DFT_00$i.f.out >> DP_DFT_f.out
		let i=i+1
		done

#RMSEtest part
cp /home/luowh35/scripts/RMSEtest.py .
python RMSEtest.py
#learn rate part
cp /home/luowh35/scripts/learn_rate.py .
python learn_rate.py
#Maxdev part
((y+=1))  #
k=$y"1"  # k = y*10 + 1
a=$(grep \"sys_idx\" ../param.json |sed -n $k'p')
b=${a#*temps}
c=${b%press*}
d=${c#*[}
e=${d%]*}
echo ${d%]*} > temp
s="$(grep -o "," temp |wc -l)"
r=$((s+=1))
for((i=1;i<=$r;i++))
	do
		echo $e | awk -F ',' '{print $'$i'}' >>01.model_devi/temp
		done
cp /home/luowh35/scripts/distribution_fmax.sh 01.model_devi/
cp /home/luowh35/scripts/MaxdevForce.py . 
cd 01.model_devi
. distribution_fmax.sh
rm temp
cp Max_Devi_F .. 
cd ..
python MaxdevForce.py

fi




#delete file
rm -r data* 
rm *.py lcurve.out Max_Devi_F DP* temp
