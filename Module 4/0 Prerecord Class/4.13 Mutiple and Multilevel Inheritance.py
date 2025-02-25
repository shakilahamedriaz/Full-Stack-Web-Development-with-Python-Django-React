"""
2. Multiple Inheritance  
   - A child class inherits from multiple parent classes.  

3. Multilevel Inheritance  
   - A child class inherits from a parent class, which itself inherits from another class.

"""

class GrandFather:
    def __init__(self,color, first_name):
        self.color = color
        self.first_name = first_name
    def gf_method(self):
        print("Im GrandFather")


class Father(GrandFather):  
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby = hobby
    
    def f_method(self):
        print("Im Father")


class Children(Father, GrandFather):
    def __init__(self, fashion,  hobby, color, first_name):
        super().__init__(hobby, color, first_name)
        self.fashion = fashion




gf1 = GrandFather("Black", "Shakil")
f1 = Father('Cricket', "Red", "Riaz")

print(f1.color)
print(f1.first_name)
print(f1.hobby)


c1 = Children("Test", "Badminton", "Yellow", "Ahamed")
c1.gf_method()
c1.f_method()
print(c1.fashion)

print(c1.color, c1.fashion, c1.first_name)