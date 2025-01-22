# PascalCase, camelCase, snake_case
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
coffee_maker = CoffeeMaker()
money_process = MoneyMachine()
is_machine_on = True

while is_machine_on:
    # TODO 1: Take the coffee order.
    user_choice = input(f"What would you like? {order.get_items()}:")

    # TODO 2: Turn Machine off
    if user_choice == "off":
        is_machine_on = False

    # TODO 3: Resource content
    elif user_choice == "report":
        coffee_maker.report()
        money_process.report()

    # TODO 4: Process Coffee and Money
    else:
        drink = order.find_drink(user_choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_process.make_payment(drink.cost):
                    print(f"Thanks for the order. Your {user_choice} will be ready soon ðŸ˜€")
                    coffee_maker.make_coffee(drink)