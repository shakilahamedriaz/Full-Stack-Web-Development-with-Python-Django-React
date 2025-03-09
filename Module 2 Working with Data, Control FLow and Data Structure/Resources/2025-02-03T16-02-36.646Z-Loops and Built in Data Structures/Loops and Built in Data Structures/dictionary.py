# Dictionary 
# Eng -> bangla shobdo
# Key Value pair
# Key gula obossoi --> immutable hote hobe, string, tuple ,int, float
# {"Rahim" : 21}
# NO indexing, mutable, value access kora jabe key diye
a = {"Rahim" : 21, "Karim" : 23, "Fahim" : 45}
a["Rahim"] = 23
a["Naim"] = 45
print(a)

# All keys list
print(a.keys())
print(a.values())

# for i in a.keys():
#     print(a[i])

# Key, Value pair print

for k,v in a.items():
    print(k, v)

# Get Function
print(a.get("Hamim", "Not Found"))
print(a)


# Dictionary Comprehension
# 1 - 5, 
# 1 : Odd
# 2 : even
a = {i : "Even" if i%2 == 0 else  "Odd" for i in range(10)}
print(a.get(4))
