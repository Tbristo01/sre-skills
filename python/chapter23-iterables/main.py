# Iterables = An object/collection that can return its elements one at a time
# allowing it to be iterated over in a loop

# list
numbers = [1, 2, 3, 4, 5, 6]


for number in numbers:
    print(number, end=" ")
print()

for number in reversed(numbers):
    print(number, end=" ")
print()
# tuple
numbers = (1, 2, 3, 4, 5, 6)

for number in numbers:
    print(number, end=" ")
print()

# set - cannot be reversed
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)
print()

# string
name = "Tishaun Bristol"


for character in reversed(name):
    print(character, end=" ")
print()
print()
# dictionary
my_dictionary = {
    "A": 1,
    "B": 2,
    "C": 3
}

for key,value in my_dictionary.items():
    print(key,"=",value)
