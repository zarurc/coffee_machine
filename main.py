MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
water_level = resources["water"]
milk_level = resources["milk"]
coffee_level = resources["coffee"]
income = 0

def print_report():
    print(f"Water: {water_level}ml")
    print(f"Milk: {milk_level}ml")
    print(f"Coffee: {coffee_level}ml")
    print(f"Money: ${income}")

def deduct_ingredients(drink_name):
    water_level -= MENU[drink_name]["ingredients"]["water"]
    milk_level -= MENU[drink_name]["ingredients"]["milk"]
    coffee_level -= MENU[drink_name]["ingredients"]["coffee"]
    
while not Off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print_report()
    elif choice == "off":
        Off = True
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if water_level < MENU[choice]["ingredients"]["water"]:
            print("Sorry, there is not enough water")
        elif milk_level < MENU[choice]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk")
        elif coffee_level < MENU[choice]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee")
        else:
            print("Please insert coins.")
            quarters_amount = int(input("How many quarters?"))
            dimes_amount = int(input("How many dimes?"))
            nickles_amount = int(input("How many nickles?"))
            pennies_amount = int(input("How many pennies?"))
            money_added = float(0.25 * quarters_amount + 0.1 * dimes_amount + 0.05 * nickles_amount + 0.01 * pennies_amount)
            if money_added < MENU[choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded")
            elif money_added == MENU[choice]["cost"]:
                income += MENU[choice]["cost"]
                # deduct_ingredients(choice)
                water_level -= MENU[choice]["ingredients"]["water"]
                milk_level -= MENU[choice]["ingredients"]["milk"]
                coffee_level -= MENU[choice]["ingredients"]["coffee"]
                print(f"Here is your {choice}")
            else:
                income += MENU[choice]["cost"]
                # deduct_ingredients(choice)
                water_level -= MENU[choice]["ingredients"]["water"]
                milk_level -= MENU[choice]["ingredients"]["milk"]
                coffee_level -= MENU[choice]["ingredients"]["coffee"]
                change = round(money_added - MENU[choice]["cost"], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice}")

