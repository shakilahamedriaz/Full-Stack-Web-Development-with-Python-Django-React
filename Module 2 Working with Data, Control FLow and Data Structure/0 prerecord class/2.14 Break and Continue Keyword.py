a = [ 1, 2, 3, 4, "a", 5, 6, 7]

for i in a:
    if type(i) == type('b'):
        break     #loop will stoped here
    print(i)

#output:
#1
#2
#3
#4
print("-------------")
#continue statement: skip/ignore 
for i in a:
    if  type(i) == type('a'):
        continue
    print(i)
