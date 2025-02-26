class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting."


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def start(self):
        return f"{self.brand} {self.model} is starting silently."


c1 = Car("Telsa", "Camry")
c2 = ElectricCar("Tesla", "V3", 1000)

print(c1.start())
print(c2.start())
print(c2.battery_size)