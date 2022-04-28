echo -n "Enter your programming level: "
read skill

if [[ $skill == 'junior' ]]; then
	echo 'your salary is 800$'
elif [[ $skill == 'middle' ]]; then
	echo 'your salary is 1500$'
elif [[ $skill == 'senior' ]]; then
	echo 'your salary is 3000$'
elif [[ $skill == 'teamlead' ]]; then
	echo 'your salary is 5000$'
else
	echo 'your salary is 7500$'
fi
