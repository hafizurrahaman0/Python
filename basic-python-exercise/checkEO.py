# program to check if a given number is even or odd

num = int(input("Enter a Number: "))

if num % 2 == 0:
    print(num, " is even")
elif num % 2 != 0:
    print(num, " is odd")
else:
    print("invalid input")