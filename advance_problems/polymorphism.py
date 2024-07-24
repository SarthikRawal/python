# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common super class. It is most commonly used with inheritance.

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

def animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)
