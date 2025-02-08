
def evensum(number):
    sm = 0
    for i in range(1, number + 1):
         if i % 2 == 0:
             sm += i
    return sm



number = int(input("Enter a number : "))
ans = evensum(number)
print(f"The even numbers sum is : ", ans)