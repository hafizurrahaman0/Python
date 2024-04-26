# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def sum_or_product(num1, num2):
    product = num1 * num2
    if product > 1000:
        return product
    else:
        return num1 + num2

print(sum_or_product(542, 30))