from menu import resources, MENU



def coffee():
    if coffee == "espresso":
        water_menu = int(MENU["espresso"]["ingredients"]["water"])
        coffee_menu = int(MENU["espresso"]["ingredients"]["coffee"])
        menu_cost = int(MENU["espresso"]["cost"])
    elif coffee == "latte":
        water_menu = int(MENU["latte"]["ingredients"]["water"])
        milk_menu = int(MENU["latte"]["ingredients"]["milk"])
        coffee_menu = int(MENU["latte"]["ingredients"]["coffee"])
        menu_cost = int(MENU["latte"]["cost"])
    elif coffee == "cappuccino":
        water_menu = int(MENU["cappuccino"]["ingredients"]["water"])
        milk_menu = int(MENU["cappuccino"]["ingredients"]["milk"])
        coffee_menu = int(MENU["cappuccino"]["ingredients"]["coffee"])
        menu_cost = int(MENU["cappuccino"]["cost"])

count = 0
if count == 0:
    water = int(resources["water"])
    milk = int(resources["milk"])
    coffe = int(resources["coffee"])
    money = 0

coffee = input(print("What would you like? (espresso/latte/cappuccino): ")).lower()
if coffee == "report":
    print(f"Water: {water} ml")
    print(f"Milk: {milk} ml")
    print(f"Coffee: {coffee} ml")
    print(f"Money: ${money}")
elif coffee == "off":
    machine_on = False
else:
    count = 1
    coffee()
    water -= water_menu
