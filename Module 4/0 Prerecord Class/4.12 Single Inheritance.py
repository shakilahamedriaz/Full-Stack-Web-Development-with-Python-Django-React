"""

Inheritance:  
- The mechanism of acquiring properties and behaviors from a parent class.

Types of Inheritance:

1. Single Inheritance  
   - A child class inherits from a single parent class.  
"""


class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
    

class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby = hobby


gf1 = GrandFather("White", "Akanda")
f1 = Father("Cricket", "Green", "Shakil")

print(f"Color {f1.color}\nHobby: {f1.hobby}\nFrist Name: {f1.first_name}")