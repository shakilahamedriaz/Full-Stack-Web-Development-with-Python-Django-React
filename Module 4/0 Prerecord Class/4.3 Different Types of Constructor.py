"""
✅ Defines a class Car with attributes brand and model
✅ Creates objects car1 and car2 using the Car class
✅ Assigns values to their attributes (brand, model)
✅ Prints object properties to see stored values
"""

# __init__() : Dunder method , Constructor - no return constructor
#  Constructor 3 types:
#    1. Default Constructor
#    2. Parameterized Constructor
#    3. Default value Constructor


class Car:

    #default constructor:
    def __init__(self):  #self ei car class er oject ke indicate kore
        self.brand = ""
        self.model = ""

    #Parameterized constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    #Default value Constructor
    def __init__(self, brand ="Brand3", model="Model3"):
        self.brand = brand
        self.model = model


print("Default constructor output: ")
car1 = Car()
car1.brand = "Brand1"
car1.model = "Model1"
print(car1.brand, car1.model)
#Brand1 Model1


print("Parameterized constructor output: ")
car2 = Car("Brand2", "Model2")
print(car2.brand, car2.model)
#Brand2 Model2

print("Default value constructor output: ")
car3 = Car()
print(car3.brand, car3.model)
#Brand3 Model3