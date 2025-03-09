# multiple method with same name, with diffrent parameters
# py doesnot support method overlaoding
# compile time polymorphism

class MathOperations:
    def add(self, a, b, c = 0):
        return a + b + c

math = MathOperations()
print(math.add(10, 20))
print(math.add(2, 3, 3))