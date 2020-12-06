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

# 1. Preguntar al usuario que le gustaría tomar
off = False
money = 0.0
while off.__eq__(False):
  coffee = input("What would you like? (espresso/latte/cappuccino): ")
  if coffee.__eq__("off"):
    off = True
  elif coffee.__eq__("report"):
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(money))
  else:
    if coffee.__eq__("espresso"):
      if ((MENU["espresso"]["ingredients"]["water"] <= resources["water"]) and
        (MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"])):
        print("Insert coins please...")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        if coins >= MENU["espresso"]["cost"]:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            change = coins - MENU["espresso"]["cost"]
            money = money + MENU["espresso"]["cost"]
            print("Here is $" + str(change) + " in change")
            print("Here is your espresso, enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")
      elif MENU["espresso"]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
      elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
      else:
        print("Sorry there are not enough coffee and water")
    elif coffee.__eq__("latte"):
      if ((MENU["latte"]["ingredients"]["water"] <= resources["water"]) and
          (MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]) and
            (MENU["latte"]["ingredients"]["milk"] <= resources["milk"])):
        print("Insert coins please...")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        if coins >= MENU["latte"]["cost"]:
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            change = coins - MENU["latte"]["cost"]
            money = money + MENU["latte"]["cost"]
            print("Here is $" + str(change) + " in change")
            print("Here is your latte, enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")
      elif MENU["latte"]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
      elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
      elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk")
      else:
        print("Sorry there are not enough coffee, water and milk")
    elif coffee.__eq__("cappuccino"):
      if ((MENU["cappuccino"]["ingredients"]["water"] <= resources["water"]) and
          (MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]) and
            (MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"])):
        print("Insert coins please...")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        if coins >= MENU["cappuccino"]["cost"]:
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            change = coins - MENU["cappuccino"]["cost"]
            money = money + MENU["cappuccino"]["cost"]
            print("Here is $" + str(change) + " in change")
            print("Here is your cappuccino, enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")
      elif MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
      elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
      elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk")
      else:
        print("Sorry there are not enough coffee, water and milk")