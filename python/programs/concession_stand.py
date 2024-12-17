menu = {
    "Classic": 2.50,
    "Caramel": 3.00,
    "Cheese": 3.25,
    "Spicy": 4.00,
    "Loaded": 5.00,
    "Jalapeno": 4.50,
    "Coke": 1.50,
    "Sprite": 1.50,
    "Water": 1.00,
    "M&Ms": 2.00,
    "Skittles": 2.00,
    "Snickers": 2.25
}
cart = []
total = 0
print("-------MENU------")
for key, value in menu.items():

    print(f"{key:10}:${value:.2f}")

print("------------------")
print()


while True:
    food = input("Select an item (q to quite): ").capitalize()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------YOUR ORDER-------")
for food in cart:
    total+=menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is :${total:.2f}")