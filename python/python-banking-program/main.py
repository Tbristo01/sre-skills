# Python Banking Program

def show_balance(balance):
    print(f"Your balance is $:{balance:.2f}")
    print()


def deposit():
    amount = float(input("Enter the amount to be deposited: $"))
    if amount < 0:
        print(f"{amount} is not a valid amount\n")
        return 0
    else:
        return amount
    print()


def withdraw(balance):
    amount = float(input("Enter the amount to be withdraw: $"))

    if amount > balance:
        print("Insufficient Funds!\n")
        return 0
    elif amount < 0:
        print("Amount is greater than 0\n")
        return 0
    else:
        return amount


def main():

    balance = 0


    is_running = True


    while is_running:
        print("BANKING PROGRAM")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter a your choice (1-4): ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()

            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("Invalid Selection!")
                print()
    print("Thank you,have a nice day!")


if __name__=="__main__":
    main()