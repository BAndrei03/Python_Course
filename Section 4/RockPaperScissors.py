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
game_images=[rock, paper, scissors]
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or subreddits for Scissors.\n"))
print(game_images[user_choice])

pc = int(random.randint(0,2))
print(game_images[pc])

if user_choice == pc:
    print("Its a tie")
elif user_choice ==0 and pc == 1:
    print("PC won")
elif user_choice ==0 and pc == 2:
    print("you won")
elif user_choice ==1 and pc == 0:
    print("You won")
elif user_choice ==1 and pc == 2:
    print("PC won")
elif user_choice ==2 and pc == 0:
    print("PC won")
else:
    print("you won")