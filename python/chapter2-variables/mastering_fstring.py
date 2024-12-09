# Mastering f-string in python
# We will cover embedding expressions, formatting numbers, aligning text, using dictionaries, and multi-line f-strings.

# Basic Usage
print("Basic Usage")
name = "Tishaun"
age = 33
print(f"Hello, my name is {name} and I am {age} years old.\n")

print(f"Embedding Expression")
a = 6
b = 14
print(f"The sum of {a} and {b} is {a+b}.\n")

# You can also call Python functions within the braces.


def get_greeting(name):
    return f"Hello, {name}!\n"


print(f"{get_greeting('Bristol')}")
"""
F-strings support number formatting options, which can be very useful for controlling the display of numerical values. 
Instead of writing multiple lines of code to format numbers manually, you can use f-strings to simplify the process. 
For example, we will display the float variable called `cost_ratio` with three decimal places. 
"""

print("Formatting Numbers")
cost_ratio = 6.5789457766
print(f"Cost ratio rounded to 3 decimal places: {cost_ratio:.3f}\n")

print("Add a thousand separators to a long series of numbers.")
house_cost = 8930000
print(f"Formatted number: {house_cost:,}\n")

print("To format a number as a percentage, use the % symbol.")
percentage = 0.25

print(f"Percentage: {percentage:.2%}\n")

print("Aligning Text")
print("""
F-strings allow you to align text to the :
left   - < 
right  - >
center - ^ 
You can also specify a width for the alignment as shown below. 
""")
id = "Id"
name = "Name"
add = "Address"
formatted_name = f"|{id:<10}|{name:>10}|{add:^10}|"
print(formatted_name)
print()

print("F-strings with Dictionaries")
print("""
F-strings can work seamlessly with dictionaries. 
We will access the dictionary keys within the curly braces.
""")
person = {"name": "Abid", "age": 33}
print(f"Name: {person['name']}, Age: {person['age']}")

print("Multiline F-strings")
print(""" 
F-strings can also be used with triple quotes to create multiline strings.
This is useful for formatting long text blocks.
""")
name_1 = "Abid"
age_1 = 33
multiline_string = f"""
Name: {name_1}
Age: {age_1}
"""
print(multiline_string)


# Reference for the code which is being use : https://www.kdnuggets.com/mastering-f-strings-in-python
