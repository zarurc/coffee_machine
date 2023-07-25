MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


Off = False
income = 0

def print_report():
    print(f"Water: {water_level}ml")
    print(f"Milk: {milk_level}ml")
    print(f"Coffee: {coffee_level}ml")
    print(f"Money: ${income}")

def deduct_ingredients(drink_name):
    water_level -= MENU[drink_name]["ingredients"]["water"]
    milk_level -= MENU[choice]["ingredients"]["milk"]
    coffee_level -= MENU[choice]["ingredients"]["coffee"]
    
    
while not Off:
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]
    
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print_report()
    elif choice == "off":
        Off = True
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if water_level < MENU[choice]["ingredients"]["water"]:
            print("Sorry, there is not enough water")
            Off = True
        elif milk_level < MENU[choice]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk")
            Off = True
        elif coffee_level < MENU[choice]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee")
            Off = True
        else:
            print("Please insert coins.")
            quarters_amount = ("How many quarters?")
            dimes_amount = ("How many dimes?")
            nickles_amount = ("How many nickles?")
            pennies_amount = ("How many pennies?")
            money_added = 0.25 * quarters_amount + 0.1 * dimes_amount + 0.05 * nickles_amount + 0.01 * pennies_amount
            if money_added < MENU[choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded")
                Off = True
            elif money_added == MENU[choice]["cost"]:
                