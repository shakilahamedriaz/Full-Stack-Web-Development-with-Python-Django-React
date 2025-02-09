 
"""
# Default Parameter:

When you define a function, you can give some parameters default values.
If the user doesn’t provide a value for those parameters, the default value 
is used.

"""

def my_name(f_name, l_name = "khan"):
    print(f_name, l_name)


my_name("Rahim")
# Rahim khan
my_name("Fahim", "Uddin")  #override hoye uddin print korbe
# Fahim Uddin


"""
# Pass Keyword:

The pass keyword is used when you need to write some code, but you don’t 
want it to do anything yet (like a placeholder). It helps avoid errors in 
empty blocks.

"""


def greetings():
    pass



"""
Pass is used when you don’t want to do anything yet in a block of code
 but need to keep the structure. """