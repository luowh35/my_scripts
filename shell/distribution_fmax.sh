#!/bin/bash
for t in `cat temp` ;do
echo $t
rm fdr.dat
grep "\"temps\": $t"  task.*/job* | awk -F '/' '{print $1}' > fdr.dat
rm ${t}K
for i in `cat fdr.dat`;do
cat ${i}/model_devi.out | awk '{print $5}' >> ${t}K
done
echo "finished collection of temperature $t "
sed -ie '/avg/d' ${t}K
done
paste *K > Max_Devi_F
