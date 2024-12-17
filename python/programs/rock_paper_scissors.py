# ROCK - PAPER- SCISSORS
import random
options = ("rock", "paper", "scissors")
num_of_games=0
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        
        player = input("Enter a choice (rock,paper,scissors): ").lower()
        num_of_games+=1
        if player.isalpha() and player in options:
            if player == computer:
                print(f"It's a Tie ! - {player} is the same {computer}.")

            elif player == "rock" and computer == "scissors":
                print(f"You WIN ! - {player} beats {computer}.")
            elif player == "paper" and computer == "rock":
                print(f"You WIN ! - {player} beats {computer}.")
            elif player == "scissors" and computer == "paper":
                print(f"You WIN ! - {player} beats {computer}.")
            else:
                print(f"You loose - {computer} beats {player}.")
       

            stop=input("\nDo you want to play another rouund (N- no, Y- yes):  ").capitalize()

            if not stop=="Y":
                print(f"Number of games played: {num_of_games}")
                running=False
            print()    
        else:
            print(f"{player} is an invalid input -use (rock,paper,scissors)")
            print()
