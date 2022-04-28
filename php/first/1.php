<?php

$a = "hello";
$b = " world";
$e = $a.$b;
$c = 5;
$d = 10;
print "$e"; 
print "\n";
print $c + $d;
$d += 5;
print "\n";
print "$d\n";
print strlen($e) . "\n";
print strtoupper($e)."\n";

if ($a == "hello"){
	print "yes\n";
}
else{
	print "no\n";
}

$arr = [1,2,3,4,5];
print $arr[1]."\n";
$arr[0] = 99;
print $arr[0]."\n";
print implode(", ", $arr)."\n";
$arr_str = implode(", ", $arr);
print_r(explode(", ", $arr_str))."\n";

 for ($i=0; $i<count($arr); $i++){
 	print $arr[$i]."\n";
 }

 print "\n";

foreach( $arr as $elem){
	print "$elem"."\n";
}


$dict = ["name" => "yaroslav", "age" => 18];
print $dict["name"]."\n";
$dict["age"] = 22;
print $dict["age"]."\n";

foreach ($dict as $key => $value){
	print "$key => $value"."\n";
}

 function add_numbers($a, $b){
 	return $a + $b;
 }

function sum_of_element_of_array($array){
	$count = 0;
	foreach( $array as $item){
		$count += $item;
	}
	return $count;
}

print "result is ".sum_of_element_of_array($arr);