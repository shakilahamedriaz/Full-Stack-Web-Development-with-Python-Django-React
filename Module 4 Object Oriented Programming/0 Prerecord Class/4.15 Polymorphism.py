"""
# Polymorphism:
   - "Poly" means multiple, and "Morphism" means forms.
   - It allows methods to have the same name but behave differently.

## Types of Polymorphism:
1. Method Overriding
2. Method Overloading
"""

# 1. Method Overriding Example

# Base Class
class GrandFather:
    def greet(self):
        print("Grandfather says: Hello!")


# Derived Class (Father) - Overrides greet() method
class Father(GrandFather):
    def greet(self):
        print("Father says: Hey there!")


# Derived Class (Children) - Overrides greet() method
class Children(Father):
    def greet(self):
        print("Children says: Hi!")


# Creating objects 
gf = GrandFather()
f = Father()
c = Children()


gf.greet()  # Calls GrandFather's greet method
f.greet()   # Calls Father's greet method (Overridden)
c.greet()   # Calls Children's greet method (Overridden)

"""
Grandfather says: Hello!
Father says: Hey there!
Children says: Hi!
"""


#2.Method Overloading
"""
Python does not support method overloading in the way some other languages (like Java or C++) do

"""
class Shape:
    def area(self, a, b=10):
        return a * b  

ob = Shape()
print(ob.area(10))     # 10 * 10 = 100
print(ob.area(12, 10)) # 12 * 10 = 120

"""
This is a simple and effective way to achieve method overloading behavior in Python!
"""


