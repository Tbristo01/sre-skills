import random


def print_dice_art(number):
    dice_faces = {
        1: (
            "+-------+",
            "|       |",
            "|   o   |",
            "|       |",
            "+-------+"
        ),
        2: (
            "+-------+",
            "| o     |",
            "|       |",
            "|     o |",
            "+-------+"
        ),
        3: (
            "+-------+",
            "| o     |",
            "|   o   |",
            "|     o |",
            "+-------+"
        ),
        4: (
            "+-------+",
            "| o   o |",
            "|       |",
            "| o   o |",
            "+-------+"
        ),
        5: (
            "+-------+",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            "+-------+"
        ),
        6: (
            "+-------+",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            "+-------+"
        ),
    }
    # Print the selected dice face
    for line in dice_faces[number]:
        print(line)


def roll_dice():
    return random.randint(1, 6)


def play_game():
    print("Welcome to the Dice Roller Game! 🎲")
    while True:
        try:
            num_dice = int(
                input("\nEnter the number of dice to roll (1-10): "))
            if not 1 <= num_dice <= 10:
                print("Please enter a number between 1 and 10.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        total = 0
        print("\nRolling the dice...")
        for i in range(num_dice):
            result = roll_dice()
            total += result
            print(f"\nDice {i+1} rolled:")
            print_dice_art(result)
            print(f"Result: {result}")

        print(f"\nTotal sum of dice rolled: {total}")

        play_again = input("\nDo you want to roll again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    play_game()
