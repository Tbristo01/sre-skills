# *args = allow you to pass multiple non-key arguments
# **kwargs= allow you to pass multiple keywords-arguments
#  unpacking operator
# 1.positonal , 2.defualt ,3.keywrod ,4.Arbitrary

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg

#     return total


# print(add(1, 43, 43, 32, 432, 13, 31, 313))

def display_name(*names):
    for name in names:
        print(name, end="-")


display_name("Tishaun", "Keston", "Bristol")
print()
display_name("MR", "Tishaun", "Keston", "Bristol")
print()


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:<6}:{value:<10}")


print_address(street="954 Albany Ave",
              apt="100",
              city="Brooklyn",
              state="NY",
              zip="11203")

print()

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    print(f"{kwargs.get('city')},{kwargs.get('state')},{kwargs.get('zip')}")


shipping_label("Mr.","Tishaun","Bristol",
               street="954 Albany Ave",
               apt="#12b",
               city="Brooklyn",
               state="New York",
               zip="11203")