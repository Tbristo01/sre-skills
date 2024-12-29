# Property Decorator - This is used to define a method as property (it can be accessed like an attribute)
# Benefit: Add additional logic when reading, writing, or deleting
# Provides better getter, setter, and deleter methods.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}"

    @property
    def height(self):
        return f"{self._height}"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width was deleted!")

    @height.deleter
    def height(self):
        del self._height
        print("Height was deleted!")


rectangle = Rectangle(3, 4)

rectangle.height = 0  # Attempt to set height to 0, should print a warning
print(rectangle.height)  # Print the height, even if it wasn't updated
print(rectangle.width)  # Print the width

del rectangle.height  # Delete the height attribute, should print confirmation
del rectangle.width  # Delete the width attribute, should print confirmation
