#   Variable = A container for a value (string , integer, float , boolean)
#              A variable behaces as if it was the value it contains
#   F-string - this is used to display a variable via a function

# string 
# name = input("Enter the your name: ")
# print(type(name),"=",name)

# integers - these are  whole number without a decimal place 
# your_score =int(input("How many points did you score today: "))
# print(type(your_score),"=",your_score)

# float - these are number with a decimal point for example GPA , Price ,etc 
# your_goa = float(input("What is your current GPA: "))
# print(type(your_goa), "=",your_goa)

# boolean - this either a True or False value 

# is_present =False
# name = input("Enter the your name: ")
# if is_present:
#     print(f"{name} is in class today.")
# else:
#     print(f"{name} did not make it to class.")


# f-string - this is way to print variables / modify them within the print function 
name = input("Enter the your name: ")

print(f"{name:^10}")
print(f"{name:<10}")
print(f"{name:>10}")