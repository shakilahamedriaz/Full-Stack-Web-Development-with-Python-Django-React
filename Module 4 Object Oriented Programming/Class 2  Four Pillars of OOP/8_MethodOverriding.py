# 1. Method Overriding Example
# runtime polymorphism

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

