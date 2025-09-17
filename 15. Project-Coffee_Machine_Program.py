
coffee_name = input("what would you like?(espresso/latte/cappuccino): ")

# print report

water = 300
milk = 200
coffee = 100
money = 0

def print_report(user_input):
    print(f"water: {remaining_water}")

def prepare_coffee(coffee_name):

    if coffee_name == "expresso":
        price = 1.50
        if water >= 50 and coffee >= 18:
            water -= 50
            coffee -= 18
        elif water < 50 and coffee >= 18:
            print("Sorry there is not enough water.")
        elif water >= 50 and coffee < 18:
            print("Sorry there is not enough coffee.")
        


    elif coffee_name == "latte":
        price = 2.50
        if water >= 200 and coffee >= 24 and milk >= 150:
            water -= 200
            coffee -= 24
            milk -= 150
        elif water < 200 and coffee >= 24 and milk >= 150:
            print("Sorry there is not enough water.")
        elif water >= 200 and coffee < 24 and milk >= 150:
            print("Sorry there is not enough coffee.")
        elif water >= 200 and coffee >= 24 and milk < 150:
            print("Sorry there is not enough milk.")
        


    elif coffee_name == "cappuccino":
        price = 3.00
        if water >= 250 and coffee >= 24 and milk >= 100:
            water -= 250
            milk -= 24
            coffee -= 100
        elif water < 250 and coffee >= 24 and milk >= 100:
            print("Sorry there is not enough water.")
        elif water >= 250 and coffee < 24 and milk >= 100:
            print("Sorry there is not enough coffee.")
        elif water >= 250 and coffee >= 24 and milk < 100:
            print("Sorry there is not enough milk.")



    input("Please insert coins")
    quaters = int(input("How many quaters? :"))
    dimes = int(input("How many dimes? :"))
    nickles = int(input("How many nickles? :"))
    pennies = int(input("How many pennies? :"))

    total_money = float((quaters+dimes+nickles+pennies)/100)

    return_money = price - total_money

    print(f"Here is ${return_money} in change")
    print(f"Here is your {coffee_name}")
