from artcalc import logo


#Add
def add(n1, n2):
    """Adunarea a doua numere"""
    return n1+n2

#Subtract
def subtract(n1, n2):
    """Scaderea a doua numere"""
    return n1-n2

#Multiply
def multiply(n1, n2):
    """Inmultirea a doua numere"""
    return n1*n2

#Divide
def divide(n1, n2):
    """Impartirea a doua numere"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)

    num1 = float(input("whats the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("whats the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1}{operation_symbol}{num2} = {answer}")
        if input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
    # operation_symbol = input("Pick another operation symbol")
    # num3 = int(input("whats the next number?: "))
    # calculation_function = operations[operation_symbol]
    # second_answer = calculation_function(calculation_function(num1, num2), num3)
    #
    # print(f"{first_answer}{operation_symbol}{num3} = {second_answer}")
calculator()