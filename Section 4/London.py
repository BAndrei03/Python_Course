# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

# randomname = random.Random(names)
#
# print(f"{randomname} have to pay this time!")
#
# lengthmamestring = int(len(names))
# print(lengthmamestring)
#
# choose = int(random.randint(1,lengthmamestring) - 1)
# person = names[choose]
#
# print(f"{person} has to pay this time!")

person_pay=random.choice(names)
print(person_pay)