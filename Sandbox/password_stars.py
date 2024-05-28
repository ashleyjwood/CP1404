MINIMUM_LENGTH = 10
password = input("Enter your password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password must be {MINIMUM_LENGTH} characters or more.")
    password = input("Enter your password: ")
for i in range(len(password)):
    print("*", end="")
print()
