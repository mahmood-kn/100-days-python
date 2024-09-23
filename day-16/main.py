""" Day 16 - OOP """
# from turtle import Turtle,Screen

# timmy= Turtle()
# my_screen=Screen()
# timmy.shape("turtle")
# timmy.color("red")
# print(my_screen.canvheight)
# print(timmy)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name",['Pikachu','Squirtle','Charmander'])
# table.add_column("Type",['Electric','Water','Fire'])
# table.align='l'
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu= Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
continue_order=True

def get_money(machine:MoneyMachine,drink:MenuItem):
    """Process the payment"""
    is_success=machine.make_payment(drink.cost)
    if is_success:
        coffee_maker.make_coffee(drink)


while continue_order:
    choice = input(f"What would you like? Type {menu.get_items()}: ")
    if choice=='report':
        coffee_maker.report()
        money_machine.report()
    elif choice =='off':
        continue_order=False
    elif choice in menu.get_items().split('/'):

        drink_dict=menu.find_drink(choice)
        is_res_suff=coffee_maker.is_resource_sufficient(drink_dict)
        if is_res_suff:
            get_money(money_machine,drink_dict)
