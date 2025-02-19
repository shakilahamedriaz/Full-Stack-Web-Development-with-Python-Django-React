
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
    def __init__(self, brand ="Brand 3", model="Model 3"):
        self.brand = brand
        self.model = model
    
    def display_info(self): #instance method
        print(f"Car Brand: {self.brand}\nCar Model: {self.model}")



car1 = Car()
car1.display_info()


car2 = Car("Brand2", "Model2")
car2.display_info()


car3 = Car()
car3.display_info()