# def main():
#     """Print a list of names and ages, and find the oldest person's name."""
#     names = ['John', 'Doe', 'Jane', 'Jack']
#     ages = [16, 76, 76, 54]
#
#     for i in range(len(names)):
#         print(f"{names[i]} is {ages[i]} years old")
#
#     find_oldest(names, ages)
#
#
# def find_oldest(names, ages):
#     """Find the oldest person's name and print the first name corresponding to that age."""
#     print(f"The oldest person's name is {names[ages.index(max(ages))]}")
#
#
# main()


############################################################################################################


# name_to_age = {"Billy": 210, "Jan": 34, "Sven": 56}
#
# ages = list(name_to_age.values())
# ages.sort()
#
# new_name = input("Enter a new name: ")
# new_age = int(input("Enter a new age: "))
# name_to_age[new_name] = new_age
#
# max_name_length = max(len(name) for name in name_to_age.keys())
# max_age_length = max(len(str(age)) for age in name_to_age.values())
#
# for name, age in name_to_age.items():
#     print(f"{name:{max_name_length}} - {age:{max_age_length}}")


############################################################################################################

