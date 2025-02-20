"""
1️⃣ Class
A blueprint for creating objects.
Defines class variables (shared across all instances).
2️⃣ Instance
A specific object created from a class.
Has instance variables (unique to each object).

"""



class School:
    School_name = "Abc High School"  # Class variable (shared by all instances)

    def __init__(self, name):
        self.student_name = name  # Instance variable (unique for each student)

# Creating two instances (objects) of the School class
sc1 = School("Rahim")
sc2 = School("Karim")

print(sc1.School_name)  # Output: Abc High School (from class variable)
print(sc1.student_name) # Output: Rahim (from instance variable)

print(sc2.School_name, sc2.student_name) 
# Output: Abc High School Karim (same class variable, different instance variable)
