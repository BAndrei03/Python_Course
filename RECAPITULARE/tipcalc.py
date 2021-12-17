#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calculator!!!")
bill = float(input(print("What was the total bill? ")))
tip_perc = int(input(print("How much would you like to give? 10, 12 or 15: ")))
people = int(input(print("How many people split the bill?")))

each_person = round(bill / people)
print(f"Each person should pay: ${each_person}")

tip_person = "{:.2f}".format(each_person * (1+tip_perc/100) - each_person)
print(f"Everyone should give a ${tip_person} tip")