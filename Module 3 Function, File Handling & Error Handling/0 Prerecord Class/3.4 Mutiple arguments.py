# Function with multiple arguments using *args
# 👉 *args collects arguments into a tuple, making the function adaptable to different input sizes.



def addition(*args):

    """
    This function takes multiple arguments and returns their sum.
    *args allows passing a variable number of arguments as a tuple.
    """
    print(args)  # Prints the tuple containing all arguments
    return sum(args)  # Returns the sum of all arguments

# Calling the function with multiple arguments
val = addition(1, 2, 30, 30)
print(val) 


"""
#output: 
(1, 2, 30, 30)
63
"""