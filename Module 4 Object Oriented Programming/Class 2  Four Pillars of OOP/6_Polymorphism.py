#Polymorphism means = same method name can have diffrent implementations in different classes

class Dog:
    def make_sound(self):
        return "bark"

class Cat:
    def make_sound(self):
        return "Mew"

#funcion using polymorphism
def Animal_sound(animal):
    return animal.make_sound()



dog = Dog()
cat = Cat()

print(Animal_sound(dog))
print(Animal_sound(cat))

print(dog.make_sound())
print(cat.make_sound())