class Animal:
    def sound(self):
        print("Animal makes sound")
        print("Im Animal class")
    

class Dog(Animal):
    def bark(self):
        print("Dog Barks")


dog = Dog()
dog.sound()
dog.bark()