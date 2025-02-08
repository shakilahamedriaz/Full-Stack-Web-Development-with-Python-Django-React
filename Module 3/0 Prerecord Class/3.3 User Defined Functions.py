

# 1.no return, no input
def my_funcion():  #funcion define
    a = 10
    b = 20
    print(a + b)

my_funcion()       #funcion has called



# 2.input, no return
def add_tow_numbers(a, b):  # a and b are the parameters
    sum = a + b
    print(sum)

add_tow_numbers(5, 20)      # 5, 20 are the arguments
 

# 3.input, return
def multiply_tow_nums(a, b):
    mul = a * b
    return mul

ans = multiply_tow_nums(5, 12)
print(ans)



# 4. no input, return
def hello():
    return "hello"

greatings = hello()
print(greatings)