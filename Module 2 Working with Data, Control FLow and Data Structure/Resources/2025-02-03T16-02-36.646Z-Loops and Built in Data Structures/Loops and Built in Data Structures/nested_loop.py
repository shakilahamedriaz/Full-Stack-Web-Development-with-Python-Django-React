a = [1,2,3]
a = [[1,2,3], [4,5,6]]

# Nested loop
# for i in a:
#     print(i, type(i))
#     for j in i:
#         print(j)
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# i er value joto, er por 1-i obdi print hobe
for i in range(1,6):
    for j in range(1,i+1): # 1,2,3,4,5
        print(j, end=" ")
    print()

# print() --> new line toiri kore
# print(end="") --> new line toiri korbe na 

# find the first number divisible by both 7 and 5 between 1 to 100
# (i % 7) and (i % 5)
# first number 
# 1 - 100, 101


for i in range(101,1, -1):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        break