"""
The Builder Design Pattern is used to construct complex objects step by step, 
separating the construction process from the actual object representation
"""

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __str__(self):  # Fixed self parameter
        return f"Computer with {self.cpu} CPU, {self.ram} RAM, {self.storage} STORAGE."
        

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
    
    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self
    
    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage)

# Client code
builder = ComputerBuilder()
computer = builder.set_cpu("Intel Core i9").set_ram("32GB").set_storage("1 TB SSD").build()
print(computer)