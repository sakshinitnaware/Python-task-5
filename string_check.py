# Code to check if the given strng is not at a number

# Defining a lambda function to check if a string represents a valid number
# It removes dots (.) and hyphens (-) before checking if the remaining characters are digits
str_check = lambda usr_str: usr_str.replace('.', '').replace('-', '').isdigit()

# Taking input from the user and storing it in the variable 'usr_str'
usr_str = input("Enter string: ")

# Calling the str_check function to verify if the input is a number
# Using an if-else statement to print the appropriate message based on the result
if str_check(usr_str) == True:
    # If the input is a number, print this message
    print(f"The given string " + usr_str + " is a number")
else:
    # If the input is NOT a number, print this message
    print(f"The given string " + usr_str + " is not a number")
