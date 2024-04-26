# program to find largest of 2 given numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
	print(num1, " is largest than ", num2)
elif num2 > num1:
	print(num2, " is largest than ", num1)
else:
	print("Both Are Equal: ", num1, " = ", num2)