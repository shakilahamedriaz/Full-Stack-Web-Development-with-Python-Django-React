""" List comprehension is a concise way to create lists using a single line of code. 
 It is faster and more readable than a traditional for loop."""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

#Normal way:
for i in a: 
    if i % 2 == 0:
        result.append(i)
print(result)


#List Comprehension:
print("After apply list comprehension: ")
new_result = [i for i in a if i % 2 == 0]
print(new_result)


#problem : those number are even, which will be squre
print("even square problem: ")
new_ans = [i**2 if i % 2 == 0 else i for i in a]
print(new_ans)