import functools      # use for filter() funcion

# anonymous funcion -- > Unnamed funcion

def square(x):
    return x * x

ans = square(5)
print(ans)


"""
Lambda Function in Python:
 -no print 
 -only return type

A lambda function is a small, anonymous (nameless) function in Python. 
It is used for quick, short operations without defining a full function 
using def """

#lemda argument : expression

square = lambda x : x*x
print(square(4))
# output: 16


add = lambda x, y: x + y
print(add(5, 3))  
# output: 8


students = [('Rahim', 60), ('Karim', 80), ('Fahim', 30 )]
print(students)
# output: [('Rahim', 60), ('Karim', 80), ('Fahim', 30)]


sorted_student = sorted(students, key= lambda x: x[1])
print(sorted_student)
# [('Fahim', 30), ('Rahim', 60), ('Karim', 80)]


##########            map(), filter(), reduce()     ##################


# 1*** map()
# Purpose: Applies a function to each item in an iterable (e.g., list, tuple) and returns a map object (an iterator).
# Use Case: When you want to transform all elements in an iterable
# Syntax: map(function, iterable)

nums = [1,2,3,4]
#sq_nums = list(map(square korte chacci, kar upor apply korte chacci sei value))
con_nums = list(map(str, nums))
print(con_nums)
# ['1', '2', '3', '4']

sq_nums = list(map(lambda x: x*x, nums))
print(sq_nums)
# [1, 4, 9, 16]




# 2*** filter()
# Purpose: Filters elements from an iterable based on a function that returns a boolean value. It only keeps elements that return True.
# Use Case: When you want to filter out elements that don't meet a condition
# Syntax: filter(function, iterable)
listhere = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2 == 0, listhere))
print(even)
# [2, 4, 6]




# 3** reduce()
# Purpose: Applies a function cumulatively to the items in an iterable. The function must take two arguments and reduce the iterable to a single value.
# Syntax: reduce(function, iterable[, initial])
# Use Case: When you want to reduce a sequence to a single value (like sum, product, etc.).

ok = [5,6,7,8]
summ = functools.reduce(lambda x,y: x+ y, ok)
print(summ)
# 26