number = float(input("Enter a number: "))

print(int(number))

d = int(input("Select decimal point: "))

print(f"With {d} decimal places: {number:.{d}f}")
print(f"As scientific notation: {number:.{d}e}")