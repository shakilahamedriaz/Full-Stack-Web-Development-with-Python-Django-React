# socpe -- > a region where a variable is accessible

x = 10 # global variable

print(x) 
# 10
def fun():
    y = 19 # local variable
    print("y :", y)
    # 19
    x = 200
    print("x :", x) # we can modified global variable inside the local but it will remain unchanged globally
    # 200

fun()
# 10
print("x : ", x)
# value: 10, 



# LEGB Rule:
# L - Local (inside function)
# E - Enclosing (nested function)
# G - Global (outside function, accessible everywhere)
# B - Built-in (Python functions like print, sum, max)


print("========================")


n = "global" #Global variable

def outer():
    n = "enclosing" # Enclosing variable
    def inner():
        global n  # global variable k update kore, and note1: see under the code: 
        #nonlocal n # enclosing funcion ke update kore
        n = "Local" # Local variable
        print(n)
      
    inner()
    print(n)  


outer()
print(n)

"""
nested fun er vetore e n print korle local ta ashbe,
but first fun er mje n print korle enclosing ta ashbe,
out of the fun , print korle global asbe.
"""


"""
note1: global keyword ta global variable ke change korte pare ,
 tar kono power nai enclosing variable k chanage koroar
"""


# global    -> global variable ke change korte pare
# nonlocal  -> enclosing ke chang korte pare not global