"""

object
1. properties
2. method


class
1.

"""

class Car:
    def __init__(self, make, model, year, price, color):
        print("Initializing a car")
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.color = color
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.price} {self.color}"
    #magic method/dunder method

    def update_price(self, new_price):
        self.price = new_price
        

car1 = Car("Subaru", "Forester", 2014, 20000, "blue")
print(car1.make)
print(car1.year)

print(car1)

car1.update_price()
