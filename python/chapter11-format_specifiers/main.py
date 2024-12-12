# format specifiers = {value:flags} format a vaule based on what flags are inserted 

price1=323423.1234
price2=-93532324.1231
price3=15323325232.34

# floating decimal point 
print("floating decimal point ")
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.1f}")
print()

# Padding 
print("Padding ")
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")
print()


# center-align
print("center-align")
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")
print()


# left-align
print("left-align")
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")
print()


# right-align
print("right-align")
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>0}")
print()


# thousands seperator 
print("thousands seperator ")
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")
print()
# Negative or Postive number
print("Negative or Postive number")
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")
print()


#Combo
print("thousands seperator ")
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
print()
