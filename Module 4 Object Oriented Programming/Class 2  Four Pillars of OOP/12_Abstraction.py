# Interface

from abc import ABC, abstractmethod

# Interface (abstract class with only abstract methods)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # No implementation, acts as an interface

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Instantiating subclasses
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark!
print(cat.make_sound())  # Output: Meow!
