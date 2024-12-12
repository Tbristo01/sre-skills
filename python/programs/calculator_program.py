# Python Calaculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"Answer: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Answer: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Answer: {result}")
elif operator == "/":
    result = num1 / num2
    print(f"Answer: {result:.2f}")
else:
    print(f"{operator.capitalize()} is not a vaild operator!")
