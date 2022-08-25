from secrets import choice
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while True:
    coffee_choices = menu.get_items()
    coffee_choice = input(f"What would you like? ({coffee_choices}): ")

    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(coffee_choice)
        if money_machine.make_payment(item.cost) and coffee_maker.is_resource_sufficient(item) == True:
            coffee_maker.make_coffee(item)
