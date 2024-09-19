""" Day 15 exercise - espresso machine """
from menu import MENU

drinks=[]
drinks_cost=[]
for key,item in MENU.items():
    drinks.append(key)
    drinks_cost.append(f"{key}(${item['cost']})")

MONEY=0
POWER='on'
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_enough_ingredient(available_resources,drink_ingredient):
    """check ingredients

    Args:
        available_resources (dict): remain resources
        drink_ingredient (dict): ingredient of chosen drink

    Returns:
        boolean: if the ingredient is enough or not
    """
    for res in available_resources:
        if available_resources[res]<=drink_ingredient[res]:
            print(f"Sorry, insufficient {res}")
            return False
    return True

def payment(chosen_drink):
    """do the payment work

    Args:
        chosen_drink (dict): chosen drink

    Returns:
        boolean: whether the payment succeed
    """
    print("Please insert coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    money_given=quarters*0.25 + dimes*0.10 + nickles*0.05 +pennies*0.01
    if money_given>= chosen_drink['cost']:
        change= money_given-chosen_drink['cost']
        if change>0:
            print(f"Here is your change: ${change:0.2f}")
        return True
    print('Unsufficient funds. Money refunded')
    return False
def make_coffee(choice,available_resources,chosen_drink,prev_money):
    """make the coffee and decrease resources

    Args:
        choice (str): user choice
        available_resources (dict): remain resources
        chosen_drink (dict): user chosen drink
        prev_money (float): current money

    Returns:
        tuple: resources, money 
    """
    print(f"Hear is your {choice}. Enjoy your drink")
    new_coffee=available_resources['coffee']-chosen_drink['ingredients']['coffee']
    new_milk=available_resources['milk']-chosen_drink['ingredients']['milk']
    new_water=available_resources['water']-chosen_drink['ingredients']['water']
    new_money=prev_money+chosen_drink['cost']
    new_resources={
        'coffee':new_coffee,
        'water':new_water,
        'milk':new_milk,
    }
    return new_resources,new_money

def report():
    """Make a report of remain resources"""
    print(f"Coffee: {resources['coffee']}g")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Money: ${MONEY}")

def turn_on_espresso_machine(available_resources,prev_money):
    """function handle espresso machine logic

    Args:
        available_resources (dict): espresso machine resource left

    Returns:
        tuple: power, remain resources
    """
    choice = input(f"What would you like? Type {', '.join(drinks_cost)}: ")
    new_resources=available_resources
    new_money=prev_money
    if choice in drinks:
        chosen_drink=MENU[choice]
        if is_enough_ingredient(available_resources,chosen_drink['ingredients']):
            is_success= payment(chosen_drink)
            if is_success:
                new_resources,new_money=make_coffee(choice,available_resources,chosen_drink,prev_money)
    else:
        if choice=='report':
            report()
        elif choice=='off':
            return 'off',new_resources,new_money
    return 'on',new_resources,new_money


while POWER=='on':
    POWER,resources,MONEY=turn_on_espresso_machine(resources,MONEY)
