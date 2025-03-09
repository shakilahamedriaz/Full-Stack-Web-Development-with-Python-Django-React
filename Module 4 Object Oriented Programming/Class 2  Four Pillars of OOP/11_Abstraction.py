##  abstract class
# Importing ABC (Abstract Base Class) and abstractclassmethod to define an abstract class
from abc import ABC, abstractclassmethod

# Abstract class
class Vehicle(ABC):  
    @abstractclassmethod
    def start(self):
        pass  # Abstract method (must be implemented in child classes)

    def fuel_type(self):
        return "Petrol or Diesel"  # Concrete method (already implemented, can be used by child classes)


# Concrete class implementing the abstract method
class Car(Vehicle):  
    def start(self):  
        return "Car starts with a key."  # Implementing the abstract method

# Another concrete class implementing the abstract method
class Bike(Vehicle):
    def start(self):
        return "Bike starts with a button"  # Implementing the abstract method


# Instantiating subclasses (Concrete classes)
car = Car()  
bike = Bike()

# Calling the implemented abstract method in Car
print(car.start())  # Output: Car starts with a key.

# Calling the concrete method inherited from the abstract class
print(car.fuel_type())  # This would return "Petrol or Diesel"

# Calling the concrete method from the parent class in Bike
print(bike.fuel_type())  # Output: Petrol or Diesel

# Calling the implemented abstract method in Bike
print(bike.start())  # Output: Bike starts with a button
