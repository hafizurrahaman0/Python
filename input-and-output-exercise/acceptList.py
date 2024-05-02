# Accept a list of 5 float numbers as an input from the user

number = []

for i in range(0, 5):
	print("Enter the", i, " element: ")
	element = float(input())
	number.append(element)

print("List: ", number)
