def coin_opration():
    def coin_check(coinName, coinValue):
        if coinName == "quarter":
            return coinValue * 0.25
        elif coinName == "dime":
            return coinValue * 0.10
        elif coinName == "nickel":
            return coinValue * 0.05
        elif coinName == "pennie":
            return coinValue * 0.01
    quarters = float(input("How many quarters :"))
    dimes = float(input("How many dimes :"))
    nickels = float(input("How many nickels :"))
    pennies = float(input("How many pennies :"))
    coin = {"quarter": quarters,
            "dime": dimes,
            "nickel": nickels,
            "pennie": pennies}
    coin_total = 0
    for keys, values in coin.items():
        coin_total += coin_check(coinName=keys, coinValue=values)
    return round(coin_total,2)
if __name__ == "__main__":
    print(coin_opration())
