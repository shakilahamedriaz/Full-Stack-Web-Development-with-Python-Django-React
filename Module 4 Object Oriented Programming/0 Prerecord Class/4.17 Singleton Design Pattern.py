"""
Design Pattern 🏗️
 -A reusable solution to common software design problems, ensuring efficiency, maintainability,
   and scalability.

Types:
🔹 Creational → Object creation (e.g., Singleton, Factory)
🔹 Structural → Class/object composition (e.g., Adapter, Decorator)
🔹 Behavioral → Object interaction (e.g., Observer, Strategy)


"""


"""
    #Singleton Design Pattern:
     -Ensures that a class has only one instance and 
      provides a global point of access to it.

"""
class Singleton:
    _instance = None  # Stores the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Create instance if not exists
        return cls._instance  # Return the same instance every time

# Create objects
s1 = Singleton()
s2 = Singleton()

# Check if both instances are the same
print(s1 is s2)  # ✅ True (Same instance)

