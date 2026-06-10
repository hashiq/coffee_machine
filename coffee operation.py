from platform import machine

from coin import coin_opration
machine =True
MENU = {
    "espresso": { "ingredients": {   "water": 50,"coffee": 18,}, "cost": 1.5,},
    "latte": {"ingredients": { "water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": { "ingredients": {"water": 250, "milk": 100,"coffee": 24, },"cost": 3.0,}
}
resources = {"water": 500,"milk": 500,"coffee": 500,"money":0}

#checking the resource for coffe
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

def reduce_stock(coffee_Name):
    if coffee_Name == "latte":
        water =  MENU[coffee_Name]["ingredients"]["water"]
        resources["water"]= resources["water"] - water
        coffee = MENU[coffee_Name]["ingredients"]["coffee"]
        resources["coffee"] = resources["coffee"] - coffee
        milk = MENU[coffee_Name]["ingredients"]["milk"]
        resources["milk"] = resources["milk"] - milk
    return resources

#machine is running or not for serve
while machine:
    user = input("What would you like? espresso/latte/cappuccino :").lower()
    cents = 0
    balance = 0
    if user == "report":
        print(resources)
    elif user == "latte":
        coffee_cost = MENU[user]["cost"]
        latte_check = check_coffee(coffeeName=user)
        if latte_check == True:
            cents = coin_opration()
            if cents >= coffee_cost:
                print(f"resource remain {reduce_stock(coffee_Name = user)}")
                balance = round(cents - coffee_cost,2)
                print(f"You owne {cents}")
                print(f"coffee {coffee_cost}")
                print(f"Here is ${balance} in chagne")
            elif cents < coffee_cost:
                print(f"insufficient amount {cents}")
                machine = False
                print("System exited")

    elif user == "espresso":
            coffee_cost = MENU[user]["cost"]
            latte_check = check_coffee(coffeeName=user)
            if latte_check == True:
                cents = coin_opration()
                if cents >= coffee_cost:
                    print(f"resource remain {reduce_stock(coffee_Name=user)}")
                    balance = round(cents - coffee_cost, 2)
                    print(f"You owne {cents}")
                    print(f"coffee {coffee_cost}")
                    print(f"Here is ${balance} in chagne")
                elif cents < coffee_cost:
                    print(f"insufficient amount {cents}")
                    machine = False
                    print("System exited")

    elif user == "cappuccino":
            coffee_cost = MENU[user]["cost"]
            latte_check = check_coffee(coffeeName=user)
            if latte_check == True:
                cents = coin_opration()
                if cents >= coffee_cost:
                    print(f"resource remain {reduce_stock(coffee_Name=user)}")
                    balance = round(cents - coffee_cost, 2)
                    print(f"You owne {cents}")
                    print(f"coffee {coffee_cost}")
                    print(f"Here is ${balance} in chagne")
                elif cents < coffee_cost:
                    print(f"insufficient amount {cents}")
                    machine = False
                    print("System exited")








