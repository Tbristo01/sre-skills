# Slot Machine Program
import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐️']
    results = []

    for _ in range(3):
        results.append(random.choice(symbols))

    return results


def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    # Example payout logic
    if len(set(row)) == 1:  # All symbols match
        return bet * 10
    elif len(set(row)) == 2:  # Two symbols match
        return bet * 2
    else:
        return 0


def main():
    balance = 100
    print("********************************************")
    print("*********WELCOME TO PYTHON SLOTS************")
    print("*********🍒    🍉   🍋   🔔   ⭐️************")
    print("********************************************")

    while balance > 0:
        print(f"Current balance is: ${balance}")
        bet = input("Place your bet amount $: ")

        if not bet.isdigit():
            print(f"{bet} is not a valid input, try again!")
            continue

        bet = int(bet)

        if bet > balance:
            print("INSUFFICIENT FUNDS.")
            continue
        if bet <= 0:
            print("BET MUST BE GREATER THAN 0.")
            continue

        balance -= bet

        # Spin the slot machine
        row = spin_row()
        print_row(row)

        # Calculate payout
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}!")
            balance += payout
        else:
            print("You lost this round.")

        # Ask if the user wants to continue
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thank you for playing! Goodbye!")
            break

    if balance <= 0:
        print("You are out of money. Better luck next time!")


if __name__ == '__main__':
    main()
