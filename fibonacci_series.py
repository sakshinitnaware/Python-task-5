# Fibonacci Series 

# Defining a lambda function to calculate the Fibonacci series recursively
# If n is 0 or 1, it returns n (base case)
# Otherwise, it returns the sum of the two preceding terms (recursive case)
series = lambda n: n if n <= 1 else series(n-1) + series(n-2)

# Taking input from the user to determine the number of terms in the Fibonacci series
n = int(input("Enter the term: "))

# Generating the Fibonacci series up to the nth term using list comprehension
# It calls the 'series' function for each value from 0 to n-1
print([series(i) for i in range(n)])

