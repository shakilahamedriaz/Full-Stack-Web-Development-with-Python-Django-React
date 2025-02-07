import math
#Write a program that calculates the area and circumference of a circle. Use π (pi) = 3.14159
r = float(input("Enter circle radus : "))
t_area = 3.1416*r*r


print(f"Area: {t_area} square units")
print(f"Area : {t_area} square units")


Circumference = 2 * math.pi * r
print(f"Circumference: {Circumference:.2f} units")


# Average Calculator
n = int(input("Enter the first score: "))
m = int(input("Enter the second score: "))
o = int(input("Enter the third score: "))

avg = (n + m + o) / 3


print(f"Average score: {avg:.2f}")
#print("Average score: " + str(avg))
