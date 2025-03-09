## implicit : automatically python will convert the data type
a = 10;
print(type(a))    # <class 'int'>

b = a + 10.15
print(b)
print(type(b))    # <class 'float'>
#output : 20.15


## explicit : we need to convert the data type

a = "10"
print(type(a))    # <class 'str'>

b = int(a)
print(type(b))   # <class 'int'>
print(b)
#output : 10

