# if =  Do some code only if some condition is True
#       Else do something else

# age = int(input("Enter your age: "))

# if age>=100:
#     print("You are tool old. ")
# elif age>=18 :
#     print("Congratulation ! You are now signed up. ")
# elif age<0:
#     print("You haven't been born yet!")
# else:
#     print("Sorry, you must be 18+ to sign up!")


# response = input("Would you like food? (Y/N): ")

# if response.capitalize()=="Y":
#     print("Have some food!")
# else:
#     print("No food for you!")

name = input("Enter your name: ")
if name == "":
    print("You did not enter a your name.")
else:
    print(f"Hello {name}!")


for_sale = True


if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")


is_available = False

if is_available:
    print("This user is on-line1!")
else:
    print("This user is currently unavaiable!")