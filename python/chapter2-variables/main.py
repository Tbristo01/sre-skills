#   Variable = A container for a value (string , integer, float , boolean)
#              A variable behaces as if it was the value it contains
#   F-string - this is used to display a variable via a function


# Strings
first_name = "Tishaun"
food = "pizza"
email = "Tishaunbristol@me.com"


# use of the f-string with strings
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is :{email}")

print()

# Integers
age = 25
quantity = 3
num_of_students = 30
print(f"You are {age} years old.")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

print()

# Floats
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")

# Boolean
print()
is_student = False
for_sale = False
is_online = True


if is_online:
    print("You are on-line")
else:
    print("You are off-line")


# Challenge - Post 4 variables (string , integer, float , boolean)

car = "BMW"
year = 2024
cost = 54900.50
is_competiton_package = True

print(f"I am buying a {car}, which is from {year}.I am going to pay ${cost} if it a M = {is_competiton_package}")