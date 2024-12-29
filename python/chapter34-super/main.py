import math


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(
            f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}."
        )


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        area = math.pi * self.radius ** 2
        print(
            f"It is a circle with a radius of {self.radius} and an area of {area:.2f}.")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        area = self.width ** 2
        print(
            f"It is a square with a width of {self.width} and an area of {area}.")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        area = 0.5 * self.width * self.height
        print(
            f"It is a triangle with a width of {self.width}, a height of {self.height}, and an area of {area}.")


# Example Usage
circle = Circle(color="Blue", is_filled=True, radius=7)
square = Square(color="Red", is_filled=False, width=22)
triangle = Triangle(color="Yellow", is_filled=True, width=5, height=10)

circle.describe()
square.describe()
triangle.describe()
