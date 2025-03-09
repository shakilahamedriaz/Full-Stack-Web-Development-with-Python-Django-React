"""A for loop in Python is used to iterate over a 
sequence (such as a list, tuple, string, or range) and execute 
  a block of code for each item in that sequence."""

#syntax :
#for variable in sequence:                 #in means include
    # Code block to execute for each item


#Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#output:
# apple
# banana
# cherr    

#Using range() with for loop:
for i in range(2, 4, 1):
    print(i)
#output:
# 2
# 3

#Iterating through a string:
for char in "Python":
    print(char)
#output:
# p
# y
# t
# h
# o
# n

#Using for loop with break and continue:
print("Using for loop  with brak and continue : ")
print("Brak: ")
for i in range(5):
    if i == 3:   # exits the loop when i is 3
        break;
    print(i)
#output: 
#0
#1
#2

#continue
print("Continue: ")
for i in range(5):
    if i == 3:
        continue
    print(i)

#output:
#0
#1
#2 
#4


#simple loop with f function:
for i in range(1001):
    print(f"Nasa is hacking ..,{i}%")
print("haha etai bastob - ripon video")
print("It's 2025 i know c, c++, java, now im learnign python haha ")
