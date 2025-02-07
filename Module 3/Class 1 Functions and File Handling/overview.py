# --------------------------------------
# Functions and File Handling in Python
# --------------------------------------

# 1. Loop to get an even number from user
while True:
    n = input("Enter an even number: ")
    n = int(n)
    if n % 2 == 0:
        print("Thank you for entering an even number")
        break
    print("Bye bye!")

# 2. Print function with different separators
print("a", "b", "c")
print("a", "b", "c", sep='')

# 3. Function definition and overriding example
def my_function():
    print("OK google")

def my_function():
    print("Same thakle shes tai ashbe")  # Overwrites previous definition

my_function()  # Calls the latest function definition

# 4. Function with return value
def add_ten(n):
    m = n + 10
    return m

x = add_ten(80)
print(x)  # Output: 90

# 5. Function with multiple parameters
def tell_me(a, b, c):
    total = a + b + c
    return total

jug = tell_me(10, 10.50, 10)
print(jug)  # Output: 30.5

# 6. File Handling - Writing to a file
with open("example.txt", "w") as file:
    file.write("This is a test file.\n")
    file.write("Hello, World!\n")

# 7. File Handling - Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("\nFile Content:\n" + content)

# 8. File Handling - Appending to a file
with open("example.txt", "a") as file:
    file.write("\nThis is an appended line.")

# 9. File Handling - Reading line by line
print("\nReading file line by line:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Removes newline characters

# 10. Empty function using pass
def ok():
    pass
