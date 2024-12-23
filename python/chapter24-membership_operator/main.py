# memebership operator = used to ttest wheather a vaule or variable is foudn in a sequence 
# (string , list , tuple, set or dictionary )
# 1. in 
# 2. not in 
# returns a boolean vlaue (TRUE OR FALSE)

word ="APPLE"

letter = input("Guess a letter in the secret word: ").capitalize()

if letter in word:
    print(f"Their is a {letter} in the secret word.")
else:
    print(f"{letter} was not found.!")


students = {"spongebob","patrick","sandy"}


student= input("Enter the name of a student: ").lower()

if student in students:
    print(f"{student} is a student.")
else:
    print(f"{student} is not a student.")

grades ={"Sandy":"A",
         "Squidward":"B",
         "Spongebob":"C",
         "Patrick":"D"}

student = input("Enter the name of a student: ").capitalize()


if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found.")


email = "tishaun.bristol@me.com"

if "@"in email and "." in email:
    print("This is a valid email!")
else:
    print("Invalid email!")