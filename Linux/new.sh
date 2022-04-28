

echo  -n "number1: "
read number1

for (( i = 0; i < $number1; i++ )); do
	echo $i
done

if [[ $number1 < 100 ]]; then
	echo "yes"
else
	echo "no"
fi