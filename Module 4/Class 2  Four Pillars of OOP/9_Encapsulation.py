# Hiding data inside a class to prevent (direct modification)
# we use private variable (__variable) for this

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # private variable
    
    def deposit(self, amount):
        self.__balance += amount
        return f"Deposit {amount}. New balance is : {self.__balance}"

    def get_balance(self):
        return self.__balance  # Getter method



account = BankAccount(5000)

print(account.get_balance())  # 5000
print(account.deposit(1000))  # Deposit 1000. New balance is : 6000
print(account.__balance)      # BankAccount' object has no attribute '__balance'
 

