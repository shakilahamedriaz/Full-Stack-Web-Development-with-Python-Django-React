# list --> packet , fol, ata, pani, tel 
# mutable --> list er item ke update korte pari, delete korte pari

a = [21,2,13,"Rahim", 8.9, 10]

a[0] = 100
a[3] = 12
a.append(102)
a.sort()
a.remove(2)
print(a)



# 1 2 3 4 5 --> Ascending --> Choto theke boro hocche
# 5 4 3 2 1 --> Descending --> Boro theke choto hocche

# List comprehension

a = [1,2,3,4,5]
a_new = [] # [1], [1,4], [1,4,9]
for i in a:
    a_new.append(i**2)
print(a_new)

# list comprehension 

a_new = [i**2 for i in a]
print(a_new)

a_new  = [i**2 for i in a if i%3 !=0] # just if
print(a_new)

b_new = ['Even' if i%2 == 0 else 'Odd' for i in a] # just if else
print(b_new)