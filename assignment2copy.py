Assignment 2
(September 18, 2020)
1)	In the Python statement x = a + 5 - b:
	•	a and b are operands an equation
	•	a + 5 - b is operator, a statement
	a)	operands, an equation
	b)	operands, an expression
	c)	operators, a statement
	d)	terms, a group

2)	Write a program to print the quotient when 9 is divided by 2.

ANS:	print(9/2)
	4.5

3)	Write a program to print the remainder when 22 is divided by 3.

ANS:	print(22%3)
	1

4)	Write a program to create two variables, store an integer value in them and run the arithmetic operations on them. Print the answers.

ANS:	a=64
	b=95
	print(a+b)
	159
	print(a-b)
	-31
	print(a*b)
	6080
	print(a/b)
	0.6736842105263158
	print(a%b)
	64
	print(a**4)
	16777216
	
5)	Write a program to create two variables, store an integer value in them and run the comparison/relational operations on them. Print the answers.

ANS:	a=24
	b=56
	print(a==b)
	False
	print(a<b)
	True
	print(a>b)
	False
	print(a<=b)
	True
	print(a>=b)
	False

6)	Write a program to create two variables. Store any integer value in them and check:
	a)	If both of them are divisible by 4 and 3. Print the answer.
	b)	If both of them are not divisible by 4 and 3. Print the answer.
	c)	If any one of them is divisible by 4 or 3. Print the answer.

7)	Write a program to create two variables. Assign any value to them using assig operator. Once the values are assigned perform the assignment operations on them. Print the result.

ANS:	a=36
	b=78
	a+=4
	print(a)
	40
	b/=6
	print(b)
	13.0
	a-=13
	print(a)
	23
	b*=8
	print(b)
	624
	a%=23
	print(a)
	13

8)	How can one check if 10 is greater than 0 and less than 20? Write a program for the same.

ANS:	print(10>0 and 10<20)
	True	

9)	Write a program to create three lists, list1, list2 and list3 containing the name of country, person and object respectively. Create another variable and assign it the value of any list of your choice from the three lists. Check if the new created list is equal to any of the list using identity operator. Also using membership operator find if the member of the list exist in that particular list or not? 

ANS:	list1=("india","japan","nepal")
	list2=("suraj","rekha","renu","yammy")
	list3=("pen","eraser","tap")
	x=("suraj","rekha","renu","yammy")
	print(list2 is x)
	True
	print(list1 is x)
	False
	print("eraser" in list3)
	True
	print("japan" not in list2)
	True
	print("japan" not in list1)
	False
