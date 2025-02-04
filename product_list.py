# code to get the product of elements of the list

# Importing the reduce function from the functools module
from functools import reduce

# Defining a list of numbers, including positive, negative, and floating-point values
lst = [11, -12, 13, -14, 15, 16.5, 20.24]  # Expected product: 120345825.6

# Defining a lambda function to multiply two numbers
product_lst = lambda x, y: x * y

# Using reduce to apply the product_lst function cumulatively to the list elements
# This will multiply all the numbers in the list together
result1 = reduce(product_lst, lst)

# Printing the final product of all elements in the list
print(result1)
