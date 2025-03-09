def my_fun(f_name, l_name, age):
    print(f"My name is {f_name} {l_name}. I am {age} years old.")


my_fun("Shakil", "Ahamed", 25)
#output: My name is Shakil Ahamed. I am 25 years old.
#but if i forgot to pass agrument without serially it cant' recognize which argument is for which parameter
my_fun(25, "Ahamed", "Shakil")
# My name is 25 Ahamed. I am Shakil years old.


#so we use: keyword argument:

my_fun(age = 25, l_name= "Ahamed", f_name= "Shakil")
# My name is Shakil Ahamed. I am 25 years old.