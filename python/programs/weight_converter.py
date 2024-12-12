# Python weight converter 

weight = float(input("Enter your weight: "))
unit =input("Kilograms or Pounds? (K or L): ")

if unit.upper()=="K":
    weight=weight*2.205
    unit = "Lbs"

elif unit.upper()=="L":
    weight=weight/2.205
    unit = "Kgs"
else:
    print(f"{unit.upper()} was not vaild")


print(f"Your weight is: {weight:.1f} {unit}")