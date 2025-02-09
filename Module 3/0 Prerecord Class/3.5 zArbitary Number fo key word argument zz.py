 # handle unknown argument with key word value

def my_fun(**kwargs):  # we can also use (**data)
     print(kwargs)
     print(f"My name is {kwargs['f_name']} {kwargs['l_name']}.I am {kwargs['age']} years old. I got {kwargs['marks']} in tha exam. I live in {kwargs['address']}")



my_fun(l_name="Riaz", age=44, f_name="shakil", noting=55, marks=553, address = "Dhaka", coader_name = "sr bro")
#funcion jekhane called hyce sekane ulta plta serial break kore called hyce, but by use 'kwargs' we can fix it

# for print(kwargs) output:
# {'l_name': 'Riaz', 'age': 44, 'f_name': 'shakil', 'noting': 55, 'marks': 553, 'address': 'Dhaka', 'coader_name': 'sr bro'}


# for print the avobe statement with string format output:
# My name is shakil Riaz.I am 44 years old. I got 553 in tha exam. I live in Dhaka



### **note:

"""

-**kwargs allows passing an arbitrary number of keyword arguments to a function.
-It stores them as a dictionary, making the function flexible.
-Unexpected arguments do not break the function but exist in kwargs.
-Accessing missing keys directly (kwargs['key']) may cause a KeyError. Use .get() to handle unknown keys safely.

"""