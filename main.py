# admin utilities
off_machine = "off"
report = "report"

# all quantities are in ml (for water and milk) and gr (for the coffee)
coffeeMenu = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "cost": 1.50
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "cost": 2.50
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "cost": 3.0
    }
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
}

resources = {
    "water": 1000.0,
    "milk": 1000.0,
    "coffee": 1000.0,
    "money": 0.0
}

coffeeOption = ["espresso", "latte", "cappuccino"]


# this function determine if there are enough resources to prepare a coffee
def determineSufficientResources(coffeeType):
    if resources.get("water") < coffeeMenu.get(coffeeType).get("water"):
        print("Sorry, there is not sufficient water...")
        return False
    elif resources.get("milk") < coffeeMenu.get(coffeeType).get("milk"):
        print("Sorry, there is not sufficient milk...")
        return False
    elif resources.get("coffee") < coffeeMenu.get(coffeeType).get("coffee"):
        print("Sorry, there is not sufficient coffee...")
        return False
    else:
        return True


# this function is to check how many coins were inserted
def processCoins():
    print("Insert your coins...")
    penny = input("How many penny you want to insert?:")
    nickel = input("How many nickel you want to insert?:")
    dime = input("How many dime you want to insert?:")
    quarter = input("How many quarter you want to insert?:")
    total = (float(penny) * coins.get("penny")) + (float(nickel) * coins.get("nickel")) + \
            (float(dime) * coins.get("dime")) + (float(quarter) * coins.get("quarter"))
    return total


# print all the resources available to work
def getReport():
    print("Water:", resources.get("water"))
    print("Milk:", resources.get("milk"))
    print("Coffee:", resources.get("coffee"))
    print("Money:", resources.get("money"))


# validate if the money inserted was enough to buy the coffee selected
def checkTransaction(moneyInserted, coffeeSelected):
    if moneyInserted >= coffeeMenu.get(coffeeSelected).get("cost"):
        change = moneyInserted - coffeeMenu.get(coffeeSelected).get("cost")
        resources["water"] = resources.get("water") - coffeeMenu.get(coffeeSelected).get("water")
        resources["coffee"] = resources.get("coffee") - coffeeMenu.get(coffeeSelected).get("coffee")
        resources["milk"] = resources.get("milk") - coffeeMenu.get(coffeeSelected).get("milk")
        resources["money"] = resources.get("money") + coffeeMenu.get(coffeeSelected).get("cost")
        print("Here is your change: $", round(change, 2))
        print("Enjoy your ", coffeeSelected)
    else:
        print("Sorry, that is not enough money. Money refunded")


# this is our main function
def coffeeMachine():
    coffee = input("What would you like? (espresso, latte, cappuccino): ")
    while coffee is not off_machine:
        if coffee.__eq__(off_machine):
            print("goodbye!")
            break
        elif coffee.__eq__(report):
            getReport()
            coffee = input("What would you like? (espresso, latte, capuccino): ")
        elif coffee.__eq__(coffeeOption[0]):
            if determineSufficientResources(coffeeOption[0]) is True:
                moneyInserted = processCoins()
                checkTransaction(moneyInserted, coffeeOption[0])
            coffee = input("What would you like? (espresso, latte, capuccino): ")
        elif coffee.__eq__(coffeeOption[1]):
            if determineSufficientResources(coffeeOption[1]) is True:
                moneyInserted = processCoins()
                checkTransaction(moneyInserted, coffeeOption[1])
            coffee = input("What would you like? (espresso, latte, capuccino): ")
        elif coffee.__eq__(coffeeOption[2]):
            if determineSufficientResources(coffeeOption[2]) is True:
                moneyInserted = processCoins()
                checkTransaction(moneyInserted, coffeeOption[2])
            coffee = input("What would you like? (espresso, latte, capuccino): ")
        else:
            print("That option is not available, please select another...")
            coffee = input("What would you like? (espresso, latte, capuccino): ")


# execute our main function
coffeeMachine()
