print(type("22342"))  # <class 'str'>
print(type("11.11"))  # <class 'str'>

print(type(10))       # <class 'int'>
print(type(10.0))     # <class 'float'>

print(type(10+3j))    # <class 'complex'>
print(type(True))     # <class 'bool'>
print(type(False))    # <class 'bool'>

print(type([1,2,3]))  # <class 'list'>
print(type((1,2,3)))  # <class 'tuple'>
print(type({1,2,3}))  # <class 'set'>
print(type({1:2,3:4}))# <class 'dict'>
print(type(None))     # <class 'NoneType'>

print(type(print))    # <class 'builtin_function_or_method'>
print(type(len))      # <class 'builtin_function_or_method'>