# object - A bundle of related attributes (variableds) and method (functions)
# ex phone , cup ,book
# you need class to create many objects

# class = (blueprint) used to design the structure and layout of an object
from car import Car


car1 = Car("BMW", 2024, "white", "False")
car2 = Car("Mercedes", 2024, "Black", "True")
car3 = Car("Audi", 2025, "Blue", "False")


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)


car1.stop()
car2.stop()
car3.stop()


car1.describe()
car2.describe()
car3.describe()