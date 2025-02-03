 #list
""" A list in Python is an ordered, mutable (changeable) collection 
     that can store multiple data types, including numbers, strings,
     and other lists """

a = [1, 2, 3, 'Naim', "apple", 8.9, 3.4]

#list mutable : can change based on index
a[0] = 100
a[2] = "Asif"

print(a)
#output: [100, 2, 'Asif', 'Naim', 'apple', 8.9, 3.4]

#size of list
print("Size of list is : ")
print(len(a))


#list(x) : function can split a string to beocme list
#S = "Hello" --> ['H', 'e', 'l', 'l, 'o']
s = "Hello"
print(list(s))
#output: ['H', 'e', 'l', 'l, 'o']


#if we want to add a value of last in list of a
a.append([1, 2, 3])
print(a)

#to find a specific value index
print(a.index("Naim"))
#output: 4

a.reverse()
print(a)