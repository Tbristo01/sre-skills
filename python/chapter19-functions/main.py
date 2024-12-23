# function = A block of reusable code 
# placed after () the function name to invote it 

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"{name} you are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()


happy_birthday("Bro",25)
happy_birthday("Tishaun",34)
happy_birthday("Joe",40)



def display_invoice(username , amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")
    print()


display_invoice("Tishaun Bristol",55," jan-21-2025")   


def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()

    return first+" "+last


result = create_name("tishaun","bristol")

print(result)