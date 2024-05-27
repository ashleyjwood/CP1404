"""
First demos for CP1404
"""
# import random  # Used in number guesser

# Name input
"""
name = input("What is your name? ")
print("Hello", name)
"""

# Subscription cost per year
"""
# cost_monthly = float(input("What is your monthly cost? "))
# cost_yearly = cost_monthly * 12
# print(f"Your monthly cost is ${cost_yearly:.2f}")
"""

# Net pay calculator
"""
income_gross = float(input("Gross Income: $"))
percent_tax = float(input("Tax Percent: "))
income_net = income_gross * (1 - (percent_tax/100))
print(f"Your net income is ${income_net:.2f}")
"""

# User age
"""
user_age = int(input("What is your age? "))
while (user_age < 0) or (user_age > 120):
    print("Sorry, please enter a valid age")
    user_age = int(input("What is your age? "))
if 0 <= user_age < 5:
    category = "baby"
elif user_age < 18:
    category = "child"
elif user_age < 66:
    category = "adult"
else:
    category = "old"
print(f"Your age {user_age} is considered {category}")
"""

# Random number guesser
"""
secret_number = random.randint(1, 5)
guess = int(input("What is your guess? "))
while guess != secret_number:
    print("Wrong! Try again.")
    guess = int(input("What is your guess? "))
    secret_number = random.randint(1, 5)
print("Congrats! You guessed the correct secret number!")
"""

# Total and average ages for known number of people (for loop)
"""
number_of_ages = int(input("How many ages do you have? "))
for i in range(1, number_of_ages+1):
    age = int(input("What is your age? "))
    total_age = + age
    average_age = total_age / number_of_ages
    print(i, f"(The total age is {age}, and the average age is {average_age:.2f}")
"""

# Total and average ages for unknown number of people (while loop)
age = int(input("What is your age? "))
ages = []
while age != -1:
    ages.append(age)
    total_age = sum(ages)
    average_age = sum(ages) / len(ages)
    print(f"The total age is {total_age}, and the average age is {average_age:.2f}")
    age = int(input("What is your age? "))
