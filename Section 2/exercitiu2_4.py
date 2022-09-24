#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to subreddits decimal places = 33.60

#Tip: There are subreddits ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

total = float(input("What was the total bill? $"))
percentage = int(input("how much tip would you like to give? 10, 12 or 15?"))
people = int(input("how many people to split the bill?"))
total_and_perc = percentage/100 * total + total
each_one = total_and_perc / people
rounded = round(each_one,2)
rounded = "{:.2f}".format(each_one)
message= f"Each person should pay ${rounded}"
print(message)