# import random

# Random width and find area
"""
length = int(input("Enter a length: "))
width = random.randint(1, length)
area = length * width
print(f"Width is {width} and area is {area}")
"""

# Print grid
"""
def print_grid(number_of_rows, number_of_columns):
    # Version 1
    # for i in range(number_of_rows):
    #     for j in range(number_of_columns):
    #         print("*", end="")
    #     print()

    # Version 2
    # for i in range(number_of_rows):
    #     print("*" * number_of_columns)

    # Version 3
    print(f"{"*" * number_of_columns}\n" * number_of_rows)


print_grid(3, 7)
print()
print_grid(2, 50)
"""

# Tuple example
"""
def get_limits():
    low = int(input("Low: "))
    high = int(input("High: "))
    return low, high


print(get_limits())


def run_tests():
    low, high = get_limits()
    print(low, high)
    print(type(low))
    

print(run_tests())  
"""

# Main Menu for name
""" module-level docstring """
"""Complete programing with the following structure
menu:
-get valid (non-empty) name
- print greeting with lines
- print secret name (random variation)
"""

"""
def main():
    name = "John Smith"
    print("Menu: ")
    choice = input(">").upper()
    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "P":
            print_greeting(name)
        elif choice == "S":
            print(print_secret_name(name))
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input(">").upper()
    print("Farewell")


def print_greeting(name):
    length = len(name)
    print_line(length)
    print(name)
    print_line(length)


def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("Invalid name")
        name = input("Name: ")
    return name


def print_line(length):
    print("-" * length)


def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print("".join(letters))


main()
"""

# Good names (didn't get checked in lecture)
"""
1. grade_calculator
2. currency_converter
3. print_report
4. calculate_average
5. is_even
6. is_user_age_negative
"""
