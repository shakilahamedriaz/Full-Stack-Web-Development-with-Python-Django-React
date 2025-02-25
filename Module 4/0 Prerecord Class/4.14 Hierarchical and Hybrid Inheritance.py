"""
    #4. Hierarchical Inheritance  
   - Multiple child classes inherit from the same parent class.  

"""

class Vehicle:
    def engine_type(self):
        print("Vehicle has an engine")



class Car(Vehicle):   #child class inherit from paren class
    def num_doors(self):
        print("Car has 4 doors")


class Truck(Vehicle): #child class inherit from paren class
    def load_capacity(self):
        print("Truck can carry 10 tons")



car1 = Car()
car1.engine_type()
car1.num_doors()


tr1 = Truck()
tr1.engine_type()
tr1.load_capacity()

"""
Output: 
Vehicle has an engine
Car has 4 doors
Vehicle has an engine
Truck can carry 10 tons

"""
"""
    #5. Hybrid Inheritance  
   - A combination of multiple types of inheritance, such as multiple and multilevel inheritance.  
   - diffrent types of inheritance use in toghter
"""

class Shape:
    def area(self):
        print("Calculating Area..")


class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple corner")


class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length *self.breadth



rec = Rectangle(10, 5)
rec.sides()
print(f"Area is : {rec.area()}")


"""
Output:
Polygon has multiple corner
Area is : 50
"""