# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
profit = 0

print('☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕')
print('☕                   Coffee Machine                  ☕')
print('☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕')


def check_ingredients(coffee_type):
    for item in coffee_type:
        if coffee_type[item] > resources[item]:
            print(f"There is not enough {item}")
            return False
        else:
            return True


def process_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))

    input_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    return input_money


def check_money(coffee_money, mon):
    if coffee_money <= mon:
        mon = mon - coffee_money
    else:
        mon = -1

    return mon

machine_status = True

while machine_status:
    # TODO 1: Take the coffee order.
    user_choice = input("What would you like? (espresso/latte/cappuccino):")

    if user_choice in MENU:
        print(f"Thanks for the order. Your {user_choice} will be ready soon 😀")
        print(f"{MENU[user_choice]['cost']} money will be needed for {user_choice}.")
        # TODO 4: Check resources:
        ingredients_status = check_ingredients(MENU[user_choice]['ingredients'])

        if ingredients_status:
            # TODO 5: Check money:
            money = process_money()
            change = check_money(MENU[user_choice]['cost'], money)

            if change == -1:
                print("Sorry! that's not enough money. Money refunded.")
            else:
                # TODO 6: Check resource content and update it.
                profit += MENU[user_choice]['cost']
                resources['water'] = resources['water']-MENU[user_choice]['ingredients']['water']
                resources['milk'] = resources['milk']-MENU[user_choice]['ingredients']['milk']
                resources['coffee'] = resources['coffee']-MENU[user_choice]['ingredients']['coffee']

                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice} ☕ Enjoy! ")
        else:
            machine_status = False
    # TODO 2: Turn off the machine
    elif user_choice == 'off':
        machine_status = False

    # TODO 3: check the resources (Milk, Water, Coffee)
    elif user_choice == 'report':
        print(f"Water : {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee : {resources['coffee']} gm")
        print(f"Money : ${profit}")
