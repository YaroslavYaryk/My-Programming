#!bin/bash

length=5
for (( i = 0; i < $length; i++ )); do
	array[i]=$i
done
for i in ${array[@]}; do
	echo ${array[$i]}
done 
