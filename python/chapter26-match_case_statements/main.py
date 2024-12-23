# Match-case statement (switch): An alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"  # Default case for invalid input


# Example usage
print(day_of_week(1))  # Output: Monday
print(day_of_week(7))  # Output: Sunday
print(day_of_week(8))  # Output: Invalid day
print(day_of_week("pizza"))  # Output: Invalid day


def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Invalid"


print(is_weekend("Sunday"))
print(is_weekend("Tuesday"))
print(is_weekend("Work"))
