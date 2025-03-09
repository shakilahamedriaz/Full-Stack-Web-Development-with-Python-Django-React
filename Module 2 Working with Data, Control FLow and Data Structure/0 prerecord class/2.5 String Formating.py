user_input = input("What is your name? ")
a = "Good morning, {}. How are you ?".format(user_input)
# when it sees the {} it will replace it with the value of user_input

print("User input is : ", user_input)
print(a)

#lets see another example

age = 25
first_name = "Shakil"
last_name = "Riaz"

txt = "My name is {first_name} {last_name}. I am {age} years old." .format(first_name= first_name, last_name = last_name, age = age)
# when it sees the {} it will replace it with the value of first_name, last_name and age
txt2 = f"My name is {first_name} {last_name}. I am {age} years old"

print(txt)
#output: My name is Shakil Riaz. I am 25 years old.
print(txt2)
#output: My name is Shakil Riaz. I am 25 years old.
#Note: f is used to format the string
