# program to generate Fibonacci series

num_terms = int(input("Enter the number of terms: "))

a = 0
b = 1

# Print the first two terms explicitly
print(a)
print(b)

# Generate the remaining terms using a loop
for i in range(2, num_terms):
  c = a + b
  print(c)
  a = b
  b = c
