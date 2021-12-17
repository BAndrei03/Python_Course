import random

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
randomcoin = random.randint(0,1)

if randomcoin == 0:
    print("Tails")
else:
    print("Head")