# if Else statements

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))




#Python Conditions

Equals							-> x == y
Not Equals						-> x != y
Less than						-> x <  y
Less than or equal to 			-> x <= y
Greater than					-> x > y
greater than or equal to 		-> x >= y


#if statement
x = 70
y = 60

if x < y:	
	print("x is greater than y")
elif x == y:
	print("x is equal to y")
else:
	print("y is not greater than x")

#elif

x = 70
y = 70

if x >y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("Error")



int(input("Examination Result :"))
100 - 90	= A
89 - 70		= B
69 - 60		= C
59 - 40		= D
30 - 10		= FAIL



result  = int(input("Examination Result:"))

if result < 100 & result > 90 :
	print("A")
elif result < 89 & result > 70 :
	print("B")
elif result < 69 & result > 60 :
	print("C")
elif result < 59 & result > 40 :
	print("D")
elif result < 30 & result > 10 :
	print("FAIL")
else:
	print("Error")



#and is logical operator

c = 50
y = 40
z = 100
if x > y and z > x:
	print("All conditions are True")

#Or is logical operator

x = 50
y = 40
z = 100
if x > y or x > y:
	print("one of the conditions is True")

#nested if is if statements in if statements

x = 50

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No, x is not greater than 20")