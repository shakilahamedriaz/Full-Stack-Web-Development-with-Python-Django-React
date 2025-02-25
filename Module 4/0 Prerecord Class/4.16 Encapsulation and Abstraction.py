"""

  #Abstraction
  - Hides implementation details  only shows the necessary features 
  - reduce complexity and increase reusability.

"""

from abc import ABC, abstractmethod

class Vehicle(ABC):  
    @abstractmethod
    def start(self):  
        pass  

class Car(Vehicle):  
    def start(self):  
        print("Car is starting...")  

car = Car()  
car.start()  # ✅ Output: Car is starting...




"""
   #Encapsulation 
   - wrapping data data & methods into a class, restricting direct access for security & integrity.

"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # ✅ Output: 1500
# print(account.__balance) ❌ Error: Private attribute
