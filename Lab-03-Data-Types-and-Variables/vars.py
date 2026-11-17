# Creating variables of different data types
name = "John Doe"  # A string
age = 25           # An integer
is_student = True  # A boolean
height = 175.5     # A float

# Printing variables and their types
print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Is Student:", is_student, "Type:", type(is_student))
print("Height:", height, "Type:", type(height))

# Numeric data types
a = 10    # Integer
b = 10.5  # Float

# Implicit casting from integer to float
result = a + b
print("Result:", result, "Type:", type(result))

# Explicit conversion from integer to string
age_str = str(age)
print("Age as string:", age_str, "Type:", type(age_str))

# Explicit conversion from string to integer
number_str = "100"
number_int = int(number_str)
print("Number:", number_int, "Type:", type(number_int))

# Case study for customer data
customer_name = "Alice Johnson"
customer_age = "30"  # Initially taken as a string
customer_membership = "True"

# Convert age to integer
customer_age = int(customer_age)
# Convert membership to boolean (do not use bool("False"), it returns True)
customer_membership = customer_membership == "True"

print("Customer Name:", customer_name, "Type:", type(customer_name))
print("Customer Age:", customer_age, "Type:", type(customer_age))
print("Customer Membership Status:", customer_membership, "Type:", type(customer_membership))
