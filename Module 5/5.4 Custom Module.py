import demo

print(demo.add(2, 5)) # 7
print(demo.mul(5, 5)) # 25

# we can import togther
from demo import add, mul

print(add(5, 5)) # 10
print(mul(2, 2)) # 4


# we can give a custom name like
from demo import add as a, mul as m
print(a(2, 2)) #4
print(m(8, 8)) #64
