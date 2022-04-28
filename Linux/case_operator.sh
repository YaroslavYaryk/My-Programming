echo -n "enter first number: "
read num1
echo -n "enter second number: "
read num2
echo -n "enter operation: "
read operation

case $operation in
	'add' )
		echo "result: $(($num1+$num2))";;
	'diff' )
		echo "result: $(($num1-$num2))";;
	'mul' )
		echo "result: $(($num1*$num2))";;
	'div' )
		echo "result: $(($num1/$num2))";;
	*)
		echo 'Unknown operation';;
		
esac										