from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_mahcine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(print(f"What would you like? {options}: "))

    if choice == "off":
        is_on = False
    elif choice == "report":
        money_mahcine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_mahcine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)