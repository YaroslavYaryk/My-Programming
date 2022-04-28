#!bin/bash

array=(1 2 3 4 5 4 32 1)

for (( i = 0; i < ${#array[@]}; i++ )); do
 	echo ${array[$i]}
done 
