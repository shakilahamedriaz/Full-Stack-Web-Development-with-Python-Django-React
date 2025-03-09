class Employee:
    company_name = "Ostad company"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  

    @property  # Getter method (Read-only access)
    def salary(self):  # Getter method
        return self._salary


    @salary.setter  # Setter method (Modifies _salary)
    def salary(self, nes_salary):  # Setter method (Fixed)
        self._salary = nes_salary  # Correct assignment




ob1 = Employee("Shakil", 100000000000)
print(ob1.salary)  # ✅ Calls getter method

ob1.salary = 50000  # ✅ Calls setter method
print(ob1.salary)  # ✅ Output: 50000
