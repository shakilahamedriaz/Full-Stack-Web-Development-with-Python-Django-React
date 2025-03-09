# {}
# key value pair
# no scope for indexing
# key gula obossoi immutable

a = {'rahim': 12, 'karim' : 14, 'fahim': 78, 1 : [1,2,3,4], 2: {3,4,5}}

#print using normally :
print(a)
#output: {'rahim': 12, 'karim' : 14, 'fahim': 78, 1 : [1,2,3,4], 2: {3,4,5}}

# type:
print(type(a))
#<class 'dist'>

#using for loop
print("key from the 'dist' :----------")
for i in a:
    print(i)
# we just get the key here:
#output: 
# rahim
# karim
# fahim
# 1
# 2

print("value from the 'dist' :---------")
for i in a.values():
    print(i)
#output:
# 12
# 14
# 78
# [1, 2, 3, 4]
# {3, 4, 5}    

#to get keys and values:
print(a.keys(), a.values())
#output:
#dict_keys(['rahim', 'karim', 'fahim', 1, 2]) dict_values([12, 14, 78, [1, 2, 3, 4], {3, 4, 5}])


#to get key value togther:
print("key and value togther: ")
for k, v in a.items():
    print(f"key Name: {k}, values : {v}")
#output:
"""
# key Name: rahim, values : 12
key Name: karim, values : 14
key Name: fahim, values : 78
key Name: 1, values : [1, 2, 3, 4]
key Name: 2, values : {3, 4, 5}    """


print("--------")
p = [1, 2, 3]
q = ["mango", "banana", "apple"]

print(dict(zip(p,q)))
#output:
#{1: 'mango', 2: 'banana', 3: 'apple'}

k = dict(zip(p,q))
#to get specific value with using key:
print(k[1])
#output: mango


