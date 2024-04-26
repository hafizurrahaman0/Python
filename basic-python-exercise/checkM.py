# program to program to demonstrate if, elif and else

marks = int(input("Enter the Marks: "))

if marks <= 600 and marks >= 500:
    print("Grade A")

elif marks <= 500 and marks >= 400:
    print("Grade B")

elif marks <= 400 and marks >= 300:
    print("Grade C")

elif marks <= 300 and marks >= 200:
    print("Grade D")

elif marks <= 200 and marks >= 0:
    print("Failed")

else:
    print("invalid input")