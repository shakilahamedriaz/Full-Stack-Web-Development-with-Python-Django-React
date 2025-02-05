#while loop
a = [1, 2, 3, 4, 5]
sum = 0
i = 0

while i < len(a):
    sum += a[i]
    i+=1

print(sum)    
#output: 15

b = [-10, 2, 10, 33, -7]
j = 0


while j < len(b):
    if b[j] < 0:
        b[j] = 0
    j+=1

print(b)    
#output: [0, 2, 10, 33, 0]


