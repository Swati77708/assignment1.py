Assignment 4
(23/09/2020)

1)	Write a program to create a variable and store a list containing the name of 10 countries. Print all the elements of the list using a for loop.

ANS:	countries=["iran","india","japan","china","pakistan","nepal","africa","australia","usa","uae"]
	for x in countries:
    		print(x)
	iran
	india
	japan
	china
	pakistan
	nepal
	africa
	australia
	usa
	uae

2)	Write a program to create a new list containing numbers from 1 to 10. Make a new list that will store the square of the numbers present in first list. Use for loop.

ANS:	n=[1,2,3,4,5,6,7,8,9,10]
	for x in n:
        	print(x**2)
	1
	4
	9
	16
	25
	36
	49
	64
	81
	100

3)	Write a program to create two empty list. One for even numbers and one for odd numbers. Store the even numbers and odd numbers in their respective list in the range 1 to 101.

ANS:	even=[]
	odd=[]
	for x in range(1,101):
	    if (x%2==0):
	        even.append(str(x))
	    else:
	        odd.append(str(x))
	print(",".join(even))
	2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100
	print(",".join(odd))
	1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99

4)	Write a program to create five empty list that will store the values of those numbers that are divisible by 2,3,4,5 and 7 respectively in the range of 1 to 200.

ANS:	a2=[]
	b3=[]
	c4=[]
	d5=[]
	e7=[]
	for x in range(1,200):
	    if(x%2==0):
	        a2.append(str(x))
	    elif(x%3==0):
	        b3.append(str(x))
	    elif(x%4==0):
	        c4.append(str(x))
	    elif(x%5==0):
	        d5.append(str(x))
	    elif(x%7==0):
	        e7.append(str(x))
	print(",".join(a2))
	print(",".join(b3))
	print(",".join(c4))	
	print(",".join(d5))
	print(",".join(e7))
	
	2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198
	3,9,15,21,27,33,39,45,51,57,63,69,75,81,87,93,99,105,111,117,123,129,135,141,147,153,159,165,171,177,183,189,195

	5,25,35,55,65,85,95,115,125,145,155,175,185
	7,49,77,91,119,133,161





