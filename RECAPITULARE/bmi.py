# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight / (height ** 2))

if BMI <18.5:
    print(f"Your BMI is {BMI}, YOu are overweight!")

elif BMI >18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, YOu are normal weight!")

elif BMI >25 and BMI < 30:
    print(f"Your BMI is {BMI}, YOu are slightly weight!")

elif BMI >30 and BMI < 35:
    print(f"Your BMI is {BMI}, YOu are obese!")

else:
    print(f"Your BMI is {BMI}, YOu are clinicall obese")