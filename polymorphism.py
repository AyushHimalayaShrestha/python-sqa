# Polymorphism -> 
class Animals:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
class Dog(Animals):
    def make_sound(self):
        return "Bark"
    
class Cat(Animals):
    def make_sound(self):
        return "Meow"
    
class Humans(Animals):
    def make_sound(self):
        return "Speak"
animals=[Dog(), Cat(), Humans()]
print(animals)
for animal in animals:
    print(animal.make_sound())