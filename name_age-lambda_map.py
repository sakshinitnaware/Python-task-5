# code to filter the age from a dictionary

# Creating a dictionary with names as keys and ages as values
data = {"sam": 16, "zeek": 28, "ram": 15, "martty": 20}

# Defining a lambda function to check if the age is 18 or below
under_age = lambda item: item[1] <= 18

# Defining a lambda function to check if the age is above 18
above_age = lambda item: item[1] > 18

# Filtering the dictionary items to get people who are 18 or younger
filter_under_age = filter(under_age, data.items())

# Extracting the names of people who are 18 or younger
result_under_age = list(map(lambda item: item[0], filter_under_age))

# Filtering the dictionary items to get people who are older than 18
filter_above_age = filter(above_age, data.items())

# Extracting the names of people who are older than 18
result_above_age = list(map(lambda item: item[0], filter_above_age))

# Printing the names of people under 18
print("people under 18:", result_under_age)

# Printing the names of people above 18
print("people above 18:", result_above_age)
