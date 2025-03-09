# 1 - 1000
# 1
# 2
# 3

# a = list(range(1,1001))
# for i in a:
#     print(i)

# for i in range(1,11):
#     print(i, end=" ")

# break, continue

# for i in range(10): # 0 - 9
#     if i > 3: # jodi i er value 3 hoy tumi loop ta thamiye dao
#         break 
#     else: # jotokkhn na obid amader if false hocche tumi print kortei thako
#         print(i)

#  roll = 3 , skip, ignore

# for i in range(10):
#     if i == 3:
#         continue # ignore koro
#     else:
#         print(i)

# 0 - 10 , 3 dara bivajjo songkha gula ke skip korbo 
for i in range(11):
    if i % 3 == 0:
        continue
    else:
        print(i)