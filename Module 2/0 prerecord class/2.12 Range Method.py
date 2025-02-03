#range()
#The range() function is used to generate a sequence of numbers. It is commonly used in loops.
a = list(range(10))
b = tuple(range(10))

print(a)
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b)
#output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#syntax of range :
# --> range(start, stop, step)
#   start → (Optional) Beginning of sequence **(default = 0)
#   stop → End of sequence **(exclusive)
#   step → (Optional) Increment value **(default = 1)

c_list = list(range(3, 9, 2))
print(c_list)
#[3, 5, 7]

d = list(range(2, 100, 2)) #100/stop porjonto jabe na
print(d)


e = list(range(100, 2, -2))
print(e)