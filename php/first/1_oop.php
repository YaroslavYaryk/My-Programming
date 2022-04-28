<?php

class Person{

	public $name;
	public $age;

	function __construct($name, $age)
	{
		$this->name = $name;
		$this->age = $age;
	}

	function getName(){
		return $this->name;
	}

	function getAge(){
		return $this->age;
	}

	function action(){
		return "Just simple action"."\n";
	} 

	function __toString()
	{
		return "Name: $this->name, Age: $this->age";
	}

	function __destruct()
	{
		print "Person destruuctor has been called\n";
	}
}

class Builder extends Person{
	
	public $action;

	function __construct($name, $age, $action)
	{
		$this->name = $name;
		$this->age = $age;
		$this->action = $action;
	}

	function action(){
		print parent::action();
		return "I'm builder and i can build";
	} 

	function __toString()
	{
		// return parent::__toString();
		return "Name: $this->name, Age: $this->age, Action: $this->action";
	}
	function __destruct()
	{
		print "Builder destruuctor has been called\n";
	}
}

class SoftwareEngineer extends Person{
	
	public $action;

	function __construct($name, $age, $action)
	{
		$this->name = $name;
		$this->age = $age;
		$this->action = $action;
	}

	function action(){
		print parent::action();
		return "I'm programmer and i can write code";
	} 

	function __toString()
	{
		// return parent::__toString();
		return "Name: $this->name, Age: $this->age, Action: $this->action";
	}
	function __destruct()
	{
		print "SoftwareEngineer destruuctor has been called\n";
	}
}

$pers = new Person("Yaroslav", 18);
print $pers."\n\n";
print $pers->getName()."\n\n";
print $pers->getAge()."\n\n";

$builder = new Builder("Yaroslav", "18", "I can build");
print $builder."\n\n";
print $builder->action()."\n\n";

$programmer = new SoftwareEngineer("Yaroslav", "18", "I can write code");
print $programmer."\n\n";
print $programmer->action()."\n\n";

