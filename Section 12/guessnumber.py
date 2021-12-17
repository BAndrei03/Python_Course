#Number Guessing Game Objectives:

import random

random_number = random.randint(1,100)
print(random_number)

# choosen_number = int(input(f"Input a number between 1 and 100:"))
# print(choosen_number)
tracking = input("wanna play the 'easy' mode or the 'harder' mode?")
# def verify():
#     if random_number == choosen_number:
#         print(f"You have gueesed the number {random_number}")
#     elif random_number > choosen_number:
#         print("Your number is too low. Pick another one")
#     else:
#         print("Your number is too high. Pick another one")
if tracking == "easy":
    turns = 10
elif tracking == "hard":
    turns = 5

while turns!=0:
    choosen_number = int(input(f"Input a number between 1 and 100:"))
    if random_number == choosen_number:
        print(f"You have gueesed the number {random_number}")
        turns = 0
    elif random_number > choosen_number:
        print("Your number is too low. Pick another one")
        turns = turns - 1
    else:
        print("Your number is too high. Pick another one")
        turns = turns - 1
    if turns != 0:
        print(f"You got {turns} left!")
print("Game over")