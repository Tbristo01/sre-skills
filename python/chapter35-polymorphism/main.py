# polymorphism - this means to "Have many forms or faces"
# Poly = Many
# Morphe = Form
from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Cirle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base*self.height*.05


class Pizza(Cirle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings


shapes = [Cirle(4), Square(5), Triangle(6, 7),
          Pizza(toppings="Pepperoni", radius=12)]


for shape in shapes:
    print(f"{shape.area()}cm^3")
