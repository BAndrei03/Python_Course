# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
# .count("a")
# .lower()
#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

tcount1 = lower_name1.count("t")
tcount2 = lower_name2.count("t")
tcount = tcount1 + tcount2

rcount1 = lower_name1.count("r")
rcount2 = lower_name2.count("r")
rcount = rcount1 + rcount2

ucount1 = lower_name1.count("u")
ucount2 = lower_name2.count("u")
ucount = ucount1 + ucount2

ecount1 = lower_name1.count("e")
ecount2 = lower_name2.count("e")
ecount = ecount1 + ecount2

true = tcount+rcount+ucount+ecount

lcount1 = lower_name1.count("l")
lcount2 = lower_name2.count("l")
lcount = lcount1 + lcount2

ocount1 = lower_name1.count("o")
ocount2 = lower_name2.count("o")
ocount = ocount1 + ocount2

vcount1 = lower_name1.count("v")
vcount2 = lower_name2.count("v")
vcount = vcount1 + vcount2

love = lcount+ocount+vcount+ecount

total = str(true) + str(love)
total = int(total)
if total < 10 or total > 90:
    print(f"Your score is {total}, you go togheter like coke and mentos")
elif total >= 40 and total<=50:
    print(f"Your score is {total}, you are alright togheter.")
else:
    print(f"Your score is {total}")