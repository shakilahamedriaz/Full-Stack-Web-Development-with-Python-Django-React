# set define inside of {} braket
# unordered set - > indexing kore value pawa jabe na
# immutable -> not changable
# no duplicate
# set() --> for unique value


#take a list
a = [1, 2, 2, 3, 4, 4, 4, 5]
s = set(a)  
# by pasing list in set, we can get unique elements
print(s)
#output: [1,2,3,4,5]

# s[0] = 100
# print(s)
# output:error:  set is immutable

# set has tow term 
# Union , Intersection

p = {1, 2, 3}
q = {2, 3, 4, 5, 6}
c = p.intersection(q)

print("Intersection of p , q is : ")
print(c)
#output: 2, 3

#Union of set: 
u = p.union(q)
print(u)
#output: {2, 3}
{1, 2, 3, 4, 5, 6}