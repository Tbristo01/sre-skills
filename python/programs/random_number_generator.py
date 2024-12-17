# Python Random Number Guessing Game

import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses =0
is_running= True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}.")
print()

while is_running:
    guess= input("Enter your guess: ")
    
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print(f"{guess} is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}.")
        elif guess<answer:
            print("Too Low!, Try Again!")
        elif guess>answer:
            print("Too High!, Try Again!")
        else:
            print()
            print(f"CORRECT! TThe answer was {answer}")
            print(f"Number of guesses:{guesses}")
            is_running=False #Ends the Game 
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}.")
