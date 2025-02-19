# 1️⃣ Define a Class (Blueprint for Objects)
class Car:
    def __init__(self, brand, model, year):  # Constructor (initializes attributes)
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):  # Method (Function inside class)
        return f"{self.year} {self.brand} {self.model}"

# 2️⃣ Create Objects (Instances of Class)
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model S", 2023)

# 3️⃣ Access Methods and Attributes
print(car1.display_info())  # Output: 2022 Toyota Corolla
print(car2.display_info())  # Output: 2023 Tesla Model S
