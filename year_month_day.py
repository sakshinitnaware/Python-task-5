# Code to extract day month and year fro a datetime object

# Importing the datetime class from the datetime module
from datetime import datetime 

# Getting the current date and time and storing it in datetime_object
datetime_object = datetime.now()

# Printing the complete current date and time
print(datetime_object)

# Defining a lambda function to extract the day from the datetime object
# The day is formatted with two digits (e.g., 01, 09, 15)
extraction_date = lambda date: f"{date.day:02d}"

# Defining a lambda function to extract the month from the datetime object
# The month is formatted with two digits (e.g., 01, 08, 12)
extraction_month = lambda date: f"{date.month:02d}"

# Defining a lambda function to extract the year from the datetime object
extraction_year = lambda date: date.year

# Printing the extracted day from the current date
print("Date is:", extraction_date(datetime_object))

# Printing the extracted month from the current date
print("Month is:", extraction_month(datetime_object))

# Printing the extracted year from the current date
print("Year is:", extraction_year(datetime_object))
