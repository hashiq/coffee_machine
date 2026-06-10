from platform import machine

from coin import coin_opration
machine =True

MENU = {
    "espresso": { "ingredients": {   "water": 50,"coffee": 18,}, "cost": 1.5,},
    "latte": {"ingredients": { "water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": { "ingredients": {"water": 250, "milk": 100,"coffee": 24, },"cost": 3.0,}
}
resources = {"water": 300,"milk": 200,"coffee": 300,"money":0}

def check_coffee(coffeeName):
    enough_resource = True
    if coffeeName == "latte":
        for ingredientName, ingredientQty in MENU[coffeeName]["ingredients"].items():
            if resources[ingredientName] >= ingredientQty:
                pass
            else:
                 print(f"Sorry there is not enough {ingredientName}")
                 enough_resource = False

    elif coffeeName == "espresso":
        for ingredientName, ingredientQty in MENU[coffeeName]["ingredients"].items():
            if resources[ingredientName] >= ingredientQty:
                pass
            else:
                 print(f"Sorry there is not enough {ingredientName}")
                 enough_resource = False
    elif coffeeName == "cappuccino":
        for ingredientName, ingredientQty in MENU[coffeeName]["ingredients"].items():
            if resources[ingredientName] >= ingredientQty:
                pass
            else:
                 print(f"Sorry there is not enough {ingredientName}")
                 enough_resource = False

    return enough_resource

while machine:
    user = input("What would you like? espresso/latte/cappuccino :").lower()
    cents = 0

    balance = 0
    if user == "report":
        print(resources)
    elif user == "latte":
        if check_coffee(coffeeName=user) == True:
            cents = coin_opration()
            if cents >= coffee_cost:
                balance = cents - coffee_cost
                print(f" you owne {cents}")
                print(f"coffee {coffee_cost}")
                print(f"Here is ${balance} in chagne")
            elif cents < coffee_cost:
                print(f"insufficient amount {cents}")
                print("System exited")
        elif check_coffee(coffeeName=user) == False:
            print(f"You owne only {cents}")
            print("running out of resource, talk  with counter")
    elif user == "espresso":
        if check_coffee(coffeeName=user) == True:
            cents = coin_opration()
            if cents >= coffee_cost:
                balance = cents - coffee_cost
                print(f"You owne {cents}")
                print(f"coffee {coffee_cost}")
                print(f"Here is ${balance} in chagne")
        elif check_coffee(coffeeName=user) == False:
            print("running out of resource, talk  with counter")
    elif user == "cappuccino":
        if check_coffee(coffeeName=user) == True:
            cents = coin_opration()
            if cents >= coffee_cost:
                balance = cents - coffee_cost
                print(f" you owne {cents}")
                print(f"coffee {coffee_cost}")
                print(f"Here is ${balance} in chagne")
            elif cents < coffee_cost:
                print(f"insufficient amount {cents}")
                print("System exited")
        elif check_coffee(coffeeName=user) == False:
            print("running out of resource, talk  with counter")
