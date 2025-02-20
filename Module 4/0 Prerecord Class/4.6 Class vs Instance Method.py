class Employee:
    company_name = "Ostad Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def display_info(self):  #instance method
        print(f"EMP name : {self.name}\nSlary: {self.salary}")


    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name

obj1 = Employee("Rahim", 30000)
obj1.display_info()
Employee.change_company_name("ABC company")
print(obj1.company_name)


obj2 = Employee("Shakil Ahamed Riaz", 40000)
obj2.display_info()
print(obj2.company_name)



"""
common rakhte class variable, class method use kori.
Unique rkahte instance variable, instance method use kori
"""