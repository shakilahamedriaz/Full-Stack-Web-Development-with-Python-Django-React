# Define a class named Car
class Car:
    def __init__(self):  # Constructor method to initialize attributes
        self.brand = ""  # Initialize brand as an empty string
        self.model = ""  # Initialize model as an empty string

# Create the first object (car1) from the Car class
car1 = Car()  # Create an instance of the Car class
car1.brand = "Toyota"  # Assign brand name
car1.model = "Corolla"  # Assign model name

# Print the details of car1
print(car1.brand)  # Output: Toyota
print(car1.model)  # Output: Corolla

# Create another object (car2) from the Car class
car2 = Car()  # Create a second instance of the Car class
car2.brand = "Honda"  # Assign brand name
car2.model = "Civic"  # Assign model name

# Print the details of car2
print(car2.brand, car2.model)  # Output: Honda Civic


"""
✅ Defines a class Car with attributes brand and model
✅ Creates objects car1 and car2 using the Car class
✅ Assigns values to their attributes (brand, model)
✅ Prints object properties to see stored values
"""