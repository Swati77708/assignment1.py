Assignment 1 (17/09/2020)

1)	Write a program to print your name, your place of stay, your stream of study, your college name in different lines. 
	
ANS:	name="Swati gokhe"
	study="MSc biotech"
	place="bhopal"
	clg_name="dr. dy patil biotechnology and bioinformatics"
	print(name)
	print(study)
	print(place)
	print(clg_name)
	Swati gokhe
	MSc biotech
	bhopal
	dr. dy patil biotechnology and bioinformatics


2)	Raj was writing a python program to do the addition of multiple numbers. He chose one variable name as “def” to store a value of 5. But when he ran the script, the program gave an error. Could you provide a possible explanation?

	a=45
	b=5
	def=5
	d=45
	print(a+b+def+d)
	def=5
     	  ^
	SyntaxError: invalid syntax
ANS:	Because def is a function.

3)	While running a program I was faced with an error several times.

if True:
print "Answer"
else:
print "No Answer"
This was the code that I was running. What can be the possible issue?

ANS:	Because after print command you did not use parantheses thats why it gives error. 

4)	What is the difference between single quote (’), double quotes (‘’) and triple quotes (‘’’)?

ANS: 	There is no difference in single or double quotes. Both representations can be used interchangeably and we does not use generally triple quotes in python.

5)	Write a program to print only the quotients of the following division:
	a)19/2	
		9.5
	(b)27/4	
		6.75
	(c) 100/3	
		33.33333333336
	(d) 20/5
		4
6)	What modifications are required in above arithmetic operation so that we get the exact result. Explain your answer.
 	
ANS:	we can use float command(//) to get the exact result.

7)	write a program to print the following sentence:
	“Python is an interactive language”
	Access the 5th, 11th, 13th , 18th and 23rd element. Which operator did you make use of? 

ANS:	str = "python is an interactive language"	
	print(str[5])
	print(str[11])
	print(str[13])
	print(str[18])
	print(str[23])
	n
	n
	i
	a
	e

8)	Write a program to print a list containing
	A)	The name of 5 countries of your choice.
		
		list=("india","japan","nepal","china","pakistan") - tuple
		list=["india","japan","nepal","china","pakistan"] - list

	B)	Access the 4th country name.

		print(list[4])
		pakistan

	C)	Print the first 2 countries.

		print(list[:2])
		('india', 'japan')

	D)	Print the last two countries.

		print(list[3:])
		('india', 'japan')

	E)	Update the list by adding 5 more countries and then print the updated list.

		print(list + ["russia","UAE","usa","africa","korea"])
		['india', 'japan', 'nepal', 'china', 'pakistan', 'russia', 'UAE', 'usa', 'africa', 'korea']
		
9)	Write a Python program to create a tuple.

ANS:	list=("india","japan","nepal","china","pakistan") - tuple

10)	Write a Python program to create a tuple with different data types.

ANS:	list=("india","japan","nepal","china","pakistan")
	num=(1,1,2,4,5,7,6)
	mixed=(2,"tub","sam",35,78,"dear")

11)	Write a Python program to add an item in a tuple.
	
ANS:	we cant add an item in a tuple.

12)	Write a Python script to add a key to a dictionary.

	script={"name":"swati","class":"msc","section":"b"}
	script["subject"]="biotech"
	print(script)
	{'name': 'swati', 'class': 'msc', 'section': 'b', 'subject': 'biotech'}

13)	Write a Python script to add a key to a dictionary.