# while loop - this will execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# if name =="":
#     print("You did not enter your name: ")
# else:
#     print(f"Hello {name}!")

# I need to tranform the program above to keep promting the user to ask for name if one is not provided .
# This is where a while loop become helpful.


# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name: ")
#     name = input("Enter your name: ")

# print(f"Hello {name}!")


# age = int(input("Enter your age: "))

# while age < 0:
#    print()
#    print("Age can't be negative.")
#    print()
#    age = input("Enter your age: ")
# print(f"You are {age} years old.")


# food = input("Enter a food you like (q to quit): ")

# while not food.upper() == "q".upper():
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit): ")
# print("Bye!")

num = int(input("Enter a number that is between 1-10: "))

while num <1 or num>10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number that is between 1-10: "))

print(f"Your number is {num}")