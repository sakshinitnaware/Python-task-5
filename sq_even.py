# Code to make new list of even number and also their squares
   

# Defining a list of integers ranging from 0 to 55
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 32, 27] 

# Defining a lambda function to check if a number is even
even_nos = lambda data: data % 2 == 0 

# Using the filter function to get only even numbers from the list
result_even = list(filter(even_nos, lst))

# Using the map function to calculate the square of each even number
sq_even = list(map(lambda data: data**2, result_even))

# Printing the even numbers filtered from the original list
print("Even numbers from the list:", result_even)

# Printing the squares of the even numbers
print("Squares of the even numbers:", sq_even)
