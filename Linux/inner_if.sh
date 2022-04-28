echo -n "Enter x coord: "
read x
echo -n "Enter y coord: "
read y


if [[ $x -gt 0 ]]; then
	if [[ $y -gt 0 ]]; then
		echo "first quater"
	else
		echo "fourth quater"
	fi
else
	if [[ $y -gt 0 ]]; then
		echo "second quater"
	else
		echo "third quater"
	fi	
fi