# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# import math
# import math as m
# from math import pi



import example

result =example.pi

print(result)


result = example.square(5)

print(result)

result = example.cuber(234)

print(result)

result = example.area(51)

print(result)

result = example.welcome()

print(result)
