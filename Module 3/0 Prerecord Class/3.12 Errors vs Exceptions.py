# Errors vs exceptions

# Compile time, Run time

# Errors  ---> compile time error
#         ---> syntax, IndentationError


# Exceptions  --> Run time error
#             --> Indexing, mistake in key, value, zero division etc


##** Errors can handeled
##** Exceptions can be handeled


# Example of error:
# print(k)
# NameError: name 'k' is not defined


# Example of Exception handling:

try:  # je code e exception thakte pare
    with open('rahim.txt', 'r') as file:
         print(file.read())

except FileNotFoundError:
    print("File not found")  # user can understand by this message