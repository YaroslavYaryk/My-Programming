#!bin/bash

array=(1 2 3 4 5 4 32 1)

i=0
while [[ i -lt ${#array[@]} ]]; do
	echo "${array[$i]}"
	i=$(( $i+1 ))
done
