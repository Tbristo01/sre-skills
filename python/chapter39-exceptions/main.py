# exceptions - This is an event which interrupts the flow of a program .
#  For example ( ZeroDvisionError, TyeError,ValueError)
# 1.Try , 2.Except ,3.Final


# 1/0 ZeroDivisionError: division by zero

# 1+"1" TypeError: unsupported operand type(s) for +: 'int' and 'str'

# int("Pizza") ValueError: invalid literal for int() with base 10: 'Pizza'


try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print(f"You cannot divide by {number}")
except ValueError:
    print(f"You cannot divide by {number}")
except Exception:
    print(f"You cannot divide by {number}")
finally:
    print("Enter numbers only please.")
