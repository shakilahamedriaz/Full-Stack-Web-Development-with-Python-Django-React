#to get solution for the above problem (immutable string) we can use the following code

a = "riaz"  #main string doesn't change
print(a.title()) 
#output: Riaz

print(a)
#output: riaz

b = a.title()  #new string is created and stored in b
print(b)
#output: Riaz
#Note: a is still the same


#some other string methods
a = "Hello"
print(a.lower())
#output: hello

print(a.upper())
#output : HEllO

print(a.swapcase())
#output: hELLOW
#changes the case of each character

print(a.replace("H", "J"))  #replace H with J
#output: Jello
name = "Shakil Ahamed Riaz"
print(name.replace("Shakil", "Md."))
#output: Md. Ahamed Riaz

print(name)
#output: Shakil Ahamed Riaz
#Note: name is still the same due to immutability

print(count("a")) #count the number of 'a' in the string
#output: 3
