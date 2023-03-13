def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar_str):
    """Convert a string formatted as $##.## to a float."""
    return float(dollar_str.replace("$", ""))


def percent_to_float(percent_str):
    """Convert a string formatted as ##% to a float."""
    return float(percent_str.replace("%", "")) / 100

main()