# program to check if a given number belongs to Fibonacci series or not

num = int(input("Enter a Number: "))

a = 0
b = 1
temp = 0

while b < num:
    temp = b
    b = a + b
    a = temp

if num == b or num == 0 or num == 1:
    print(f"The {num} is Fibonacci Number")
else:
    print(f"The {num} is not Fibonacci Number")