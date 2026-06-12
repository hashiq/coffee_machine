from coin import coin_opration
machine =True
MENU = {
    "espresso": { "ingredients": {   "water": 50,"coffee": 18,}, "cost": 1.5,},
    "latte": {"ingredients": { "water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": { "ingredients": {"water": 250, "milk": 100,"coffee": 24, },"cost": 3.0,}
}
resources = {"water": 500,"milk": 300,"coffee": 100,"money":0}


#checking the resource for coffe
def check_coffee(coffeeName):
    ingredients= MENU[coffeeName]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"sorry we dont have: {item} ")
            return False
    return True



def reduce_stock(coffe_menu):
    ingredients= MENU[coffe_menu]["ingredients"]
    for items in ingredients:
        resources[items] -=ingredients[items]



# machine is running or not for serve
while machine:

    user = input("Welcome to windys coffee\nWhat would you like? espresso/latte/cappuccino :").lower()
    #report
    if user == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk  : {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${resources['money']}")
        print("\n"*3)

    #MACHINE OFF OR ON
    elif user == "off":
        print("power turned off ")
        machine = False
     #CHECK MENUS matching WITH USER
    elif user in MENU:
        coffee_cost = MENU[user]["cost"]
        coffee_check = check_coffee(coffeeName=user)
        if coffee_check :
            dollars = coin_opration()
            if dollars >= coffee_cost:
                resources["money"] += coffee_cost
                reduce_stock(coffe_menu = user)
                balance = round(dollars - coffee_cost, 2)
                print(f"coffee {coffee_cost}")
                print(f"You owe {dollars}")
                print(f"Here is ${balance} in change")
                print(f"Here is your {user} ☕ Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded ${dollars}")
    else:
        print(" :) please put a valid input")
        print("Thank you")
        print(" \n"*3)