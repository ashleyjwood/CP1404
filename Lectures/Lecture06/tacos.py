class User:
    def __init__(self, name="", number_of_tacos=5, score=0):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def give_taco(self, other_user):
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            other_user.score += 1
            other_user.number_of_tacos += 1
        else:
            print(f"{self.name} has no tacos left to give!")

    def __str__(self):
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left"


# Example usage
user1 = User(name="Ben")
user2 = User(name="Alice")

print(user1)  # Ben, 0 points, 5 tacos left
print(user2)  # Alice, 0 points, 5 tacos left

user1.give_taco(user2)
print(user1)  # Ben, 0 points, 4 tacos left
print(user2)  # Alice, 1 point, 6 tacos left

user2.give_taco(user1)
user2.give_taco(user1)
user2.give_taco(user1)
print(user1)  # Ben, 3 points, 7 tacos left
print(user2)  # Alice, 1 points, 3 tacos left
