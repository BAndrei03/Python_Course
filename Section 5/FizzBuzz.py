sum = 0
for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        # number = "FizzBuzz"
        print("FizzBuzz")
    elif number % 3 == 0:
        # number = "Fizz"
        print("Fizz")
    elif number % 5 == 0 :
        # number = "Buzz"
        print("Buzz")
    else:
        print(number)