# dictionary = collection of {key:value} pairs 
# ordered adn changeable . No duplicates

capital = {
    "Algeria": "Algiers",
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Belgium": "Brussels",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "China": "Beijing",
    "Denmark": "Copenhagen",
    "Egypt": "Cairo",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Mexico": "Mexico City",
    "Morocco": "Rabat",
    "Netherlands": "Amsterdam",
    "Nigeria": "Abuja",
    "Norway": "Oslo",
    "Pakistan": "Islamabad",
    "Russia": "Moscow",
    "Saudi Arabia": "Riyadh",
    "South Africa": "Pretoria",
    "South Korea": "Seoul",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Turkey": "Ankara",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Vietnam": "Hanoi"
}

# print(dir(capital))
# print(help(capital))

# print(capital.get("Vietnam"))
# print(capital.get("Sweden"))
# print(capital.get("Guyana"))


# if capital.get("Guyana"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capital.update({"Guyana":"GeorgeTown"})

# capital.update({"Vietnam":"Ho Chi Men"})

# capital.pop("China")

# capital.popitem()

# capital.clear()
# keys=capital.keys()

# for key in capital.keys():
#     print(keys)

# values = capital.values()

# for value in capital.values():
#     print(value)

for key , value in capital.items():
    print(f"{key:15}:{value:15}")