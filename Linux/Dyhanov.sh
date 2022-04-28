#!/bin/bash
filename="Диханов"
echo "Виводимо інформацію про користувача"

while read line; do
echo $line
# sleep 2s
done < $filename

echo -n "enter path to go in: "
read path
cd $path
echo
ls 