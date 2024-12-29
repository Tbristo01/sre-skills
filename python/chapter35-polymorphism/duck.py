# Duck Typing = Another way to achieve polyorphism beside inheritance
# Object must have the minimum necessary attributes /methods
# "If it looks like a duck and quack like a duck ,it must be a duck"

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car(Animal):
    def speak(self):
        print("HONK!")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
