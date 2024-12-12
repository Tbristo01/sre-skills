# validate user input exercise 
# 1 - username is no more than 12 characters 
# 2 - username must not contain space
# 3 - username must contain digits


user_name=input("Enter a username: ")

if len(user_name)>12:
    print(f"{user_name} is more that 12 characters")
elif not user_name.find(" ")==-1:
    print("Your username contains a space")
elif not user_name.isalpha():
    print("Your username is contains numbers")
else:
    print(f"This is my username : {user_name} with a length of {len(user_name)}")