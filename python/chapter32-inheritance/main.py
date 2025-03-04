# inheritance - Allows a class to inheritance attributes and methods from another class
# helps with code reuseablity and exenteibility
# class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is asleep.")


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQUEAK!")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")


print(cat.name)
print(cat.is_alive)
cat.sleep()
cat.speak()
print()
print(dog.name)
print(dog.is_alive)
dog.sleep()
dog.speak()
