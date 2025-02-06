# Combining strings (Concatenation)
first_name = "Alex"
last_name = "Smith"

full_name = first_name + " " + last_name
print(full_name)
#output: Alex Smith



# Repeating strings
print("Hip " * 2)
#output:Hip Hip

print("Hip " * 2 + "Hooray!")
#output : Hip Hip Hooray!
print("-" * 20 + "dot 20 times!")
#shows :--------------------dot 20 times!


#F-strings (formatted strings)
name = "Shakil Ahamed Riaz"
age = 15
print(f"My name is {name} and I am {age} yeas old")
