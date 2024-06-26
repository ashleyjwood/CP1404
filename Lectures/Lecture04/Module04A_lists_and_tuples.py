from operator import itemgetter

# # List names
# names = ["John", "Jane", "George", "Michael", "Steve", "Henry"]
# name_number = int(input(f"Enter number, up to {len(names)}: "))
#
# try:
#     if len(names) >= name_number > 0:
#         print(names[name_number - 1])
#     else:
#         raise IndexError
# except IndexError:
#     print("Invalid input")

# # List scores
# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
#
# new_pair = input("Enter name and score pair (E.g., John 10): ")
# new_pair = new_pair.split(' ')
# new_pair[1] = int(new_pair[1])
# score_pairs.append(new_pair)
# .sort(key=itemgetter(1), reverse=True)
# print(score_pairs)

# # For single in plurals
# text = "This is a sentence"
# long_words = [word for word in text.split() if len(word) > 3]
# print(long_words)


