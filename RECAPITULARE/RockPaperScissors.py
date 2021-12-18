import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

list=[rock, paper, scissors]

player = int(input("What would you like to pick? 0 for rock, 1 for paper, 2 for scissors: "))
computer = random.choice(list)

print(list[player])
print("vs")
print(computer)

if list[player] == computer:
    print("Its a draw!")
elif list[player] == rock and computer == paper:
    print("You won!")
elif list[player] == rock and computer == rock:
    print("Computer won!")
elif list[player] == paper and computer == rock:
    print("You won!")
elif list[player] == paper and computer == scissors:
    print("Computer won!")
elif list[player] == scissors and computer == paper:
    print("You won!")
elif list[player] == scissors and computer == rock:
    print("Computer won!")