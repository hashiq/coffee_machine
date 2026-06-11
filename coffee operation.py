from coin import coin_opration
machine =True
MENU = {
    "espresso": { "ingredients": {   "water": 50,"coffee": 18,}, "cost": 1.5,},
    "latte": {"ingredients": { "water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": { "ingredients": {"water": 250, "milk": 100,"coffee": 24, },"cost": 3.0,}
}
resources = {"water": 500,"milk": 500,"coffee": 100,"money":0}


#checking the resource for coffe
def check_coffee(coffeeName):
    enugh_resource =True
    ingredients= MENU[coffeeName]["ingredients"]

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"sorry we dont have: {item} ")
            enugh_resource = False
    return enugh_resource




def reduce_stock(coffe_menu):
    ingredients= MENU[coffeeName]["ingredients"]
  #-----------------------------------------------#
  #enter reduce stock here
    # -----------------------------------------------#

    return resources


# machine is running or not for serve
while machine:
    cents = 0
    balance = 0
    user = input("What would you like? espresso/latte/cappuccino :").lower()
    #report
    if user == "report":
        print(resources)

    #MACHINE OFF OR ON
    elif user == "off":
        print("power turned off ")
        machine = False
     #CHECK MENUS matching WITH USER
    elif user in MENU:
        coffee_cost = MENU[user]["cost"]
        coffee_check = check_coffee(coffeeName=user)
        if coffee_check == True:
            cents = coin_opration()
            if cents >= coffee_cost:
                resources["money"] += coffee_cost
                reduce_stock(coffe_menu = user)
                balance = round(cents - coffee_cost, 2)
                print(f"coffee {coffee_cost}")
                print(f"You owe {cents}")
                print(f"Here is ${balance} in change")
                print(f"Here is your {user} ☕ Enjoy!")
                print(resources)
            elif cents < coffee_cost:
                print(f"insufficient amount {cents}")
                machine = False
                print("System exited")
