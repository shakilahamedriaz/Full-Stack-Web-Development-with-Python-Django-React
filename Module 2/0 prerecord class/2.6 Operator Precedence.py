a = 4 + 5       #addition
b = 4 - 5       #subtraction
c = 4 * 5       #multiplication


d = 21 / 5      ##float division
#d = 4.2
e = 21 // 5     ##integer division
#e = 4
f = 5**2        #exponentiation 5^2 = 25


print(a, b, c, d, e)
#output: 9 -1 20 4.2 4
print(float(e))
print("actul d is 4.2 but after use int tpecasting d become", int(d))


#For sequence of operation, we learn BODMAS rule in our school life
#BODMAS rule is used to decide the sequence of operation

#B = Brackets first (parentheses) 
#O = Orders (i.e. powers and square roots, etc.)
#D = Division       /
#M = Multiplication *
#A = Addition      +
#S = Subtraction   -

#Example: (2+4) - 5 + 18 /2 + 12 * 2 - 5**2
#        = 6    - 5  +9.0   + 24     - 25 