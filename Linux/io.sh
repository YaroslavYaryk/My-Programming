#!bin/bash

write_to_file(){
	echo "hello world" > hello.txt; #just add and every time owerwrite
	# echo "hello world" >> hello.txt; #append

	echo "successfully done"
}

get_info_from_file(){
	while  read text ; do
		echo $text
	done < ./hello.txt
}

write_to_file
echo

get_info_from_file