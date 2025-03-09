class Employee:
    company_name = "Ostad company"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary #by convention, _variable name eta dhora hoy private variable, but logially eta priate hoy na

    

    def get_salary(self, password):
        if password == "admin":
            print(self._salary)
        else:
            print("Invalid Access!!")



    def set_salary(self, password, salary):
        if password == "admin":
            self._salary = salary
            print(f"New Salary : {self._salary}")
        else:
            print("Invalid Access!!!")




ob1 = Employee("Rahim", 30000)
bo2 = Employee("Karim", 50000)

#ob1._salary = 60000

#print(ob1._salary)
#output: 60000 


ob1.get_salary("admin")
ob1.set_salary("admin", 90000)
