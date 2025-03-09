class MathUtils:

    
    @staticmethod
    def add(a, b):  # No 'self' or 'cls'
        return a + b  

# Calling the static method without creating an object
print(MathUtils.add(5, 3))  # Output: 8

# Calling via an instance (still works)
obj = MathUtils()
print(obj.add(10, 7))  # Output: 17
