"""
1️⃣ Association

📌 Definition:
    -A general relationship between two independent classes.
    -No ownership—both objects can exist independently.
    -It is a "uses-a" relationship.


     Example: A Teacher and a Student are associated with each other,
     but they can exist separately.

"""

#student, laptop class
class Laptop:
    def __init__(self, brand):
        self.brand = brand



class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj

    def show_laptop_info(self):
        print(f"{self.name} has a laptop named {self.laptop_v.brand}")


print("Association: ")
lp1 = Laptop("Dell")
student1 = Student("Shakil Ahamed Riaz", lp1)
student1.show_laptop_info()



""""
2️⃣ Aggregation
📌 Definition:
    -A weak "has-a" relationship where one class contains another.
    -The contained object can exist independently of the container.
    -Partial ownership (not a strong dependency).


    Example: A Department has Teachers, but teachers can exist without a department.
"""

class Department:
    def __init__(self, name):
        self.name = name


class Univeristy:
    def __init__(self, name):
        self.name = name
        self.department = []
    
    def add_department(self, department):
        self.department.append(department)
    

    def show_department(self):
        return [department.name for department in self.department]

print("Aggregation: ")

uni1 = Univeristy("Daffodil International University")
dep1 = Department("Software Engineering")
dep2 = Department("Computer Science Department")


uni1.add_department(dep1)
uni1.add_department(dep2)

print(uni1.show_department())




"""
    3️⃣ Composition
     Definition:
    -A strong "has-a" relationship (stronger than aggregation).
    -The contained object CANNOT exist without the container.
    -Full ownership: If the container is deleted, the contained objects are also deleted.

     Example:A Car has an Engine, and the engine cannot exist separately from the car.
"""

class Engine:
    def __init__(self,  power):
        self.power = power


class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def show_details(self):
        print(f"{self.brand}  has an engine with {self.engine.power}")


print("Composition: ")
car = Car("Toyota", 100)
car.show_details()




"""


OUTPUT: 
Association: 
Shakil Ahamed Riaz has a laptop named Dell
Aggregation:
['Software Engineering', 'Computer Science Department']
Composition:
Toyota  has an engine with 100


"""