# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)
years = 90 - age_int
days = years * 365
months = years * 12
weeks = years * 42

message = f"you have {days} days, {months} months or {weeks} weeks to live until 90 years"
print(message)