# # Write your code here
"""
Objectives
Write a program that will work endlessly to make coffee for all interested
persons until the shutdown signal is given.
Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee.
If the coffee machine doesn't have enough resources to make coffee,
the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step —
if the user types "buy" to buy a cup of coffee and then changes his mind,
they should be able to type "back" to return into the main cycle.
Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
> fill

Write how many ml of water do you want to add:
> 1000
Write how many ml of milk do you want to add:
> 0
Write how many grams of coffee beans do you want to add:
> 0
Write how many disposable cups of coffee do you want to add:
> 0

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
> take

I gave you $564

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money

Write action (buy, fill, take, remaining, exit):
> exit
"""

def print_actions(ingredients):
    print(f"""
    The coffee machine has:
    {ingredients['water']} of water
    {ingredients['milk']} of milk
    {ingredients['coffee_beans']} of coffee beans
    {ingredients['coffee_cups']} of disposable cups
    {ingredients['money']} of money
    """)

    return ingredients


def enough(ingredients, requirements):
    if ingredients['water'] >= requirements['water']:
        if ingredients['milk'] >= requirements['milk']:
            if ingredients['coffee_beans'] >= requirements['coffee_beans']:
                if ingredients['coffee_cups'] >= requirements['coffee_cups']:
                    print('I have enough resources, making you a coffee!')
                    ingredients['water'] -= requirements['water']
                    ingredients['milk'] -= requirements['milk']
                    ingredients['coffee_beans'] -= requirements['coffee_beans']
                    ingredients['coffee_cups'] -= requirements['coffee_cups']
                    ingredients['money'] += requirements['money']
                else:
                    print('Sorry, not enough cups!')
            else:
                print('Sorry, not enough beans!')
        else:
            print('Sorry, not enough milk!')
    else:
        print('Sorry, not enough water!')

    return ingredients


def buy(ingredients):
    question = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    if question == '1':
        requirements = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'coffee_cups': 1, 'money': 4}
        enough(ingredients, requirements)

    elif question == '2':
        requirements = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'coffee_cups': 1, 'money': 7}
        enough(ingredients, requirements)

    elif question == '3':
        requirements = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'coffee_cups': 1, 'money': 6}
        enough(ingredients, requirements)

    elif question == 'back':
        pass


def fill(ingredients):
    water_ques = input("Write how many ml of water do you want to add: ")
    milk_ques = input("Write how many ml of milk do you want to add: ")
    beans_ques = input("Write how many grams of coffee beans do you want to add: ")
    cups_ques = input("Write how many disposable cups of coffee do you want to add: ")
    ingredients['water'] += int(water_ques)
    ingredients['milk'] += int(milk_ques)
    ingredients['coffee_beans'] += int(beans_ques)
    ingredients['coffee_cups'] += int(cups_ques)

    # print_actions(ingredients)

def take(ingredients):
    print("I gave you", ingredients['money'])
    ingredients['money'] -= ingredients['money']
    # print_actions(ingredients)

def remaining(ingredients):
    print_actions(ingredients)

def main():
    water = 400
    milk = 540
    coffee_beans = 120
    coffee_cups = 9
    money = 550

    ingredients = {'water': water, 'milk': milk, 'coffee_beans': coffee_beans, 'coffee_cups': coffee_cups,
                   'money': money}

    again = True
    while again:
        initial = input("Write action (buy, fill, take, remaining, exit): ")
        if initial == 'buy':
            buy(ingredients)
        elif initial == 'fill':
            fill(ingredients)
        elif initial == 'take':
            take(ingredients)
        elif initial == 'remaining':
            remaining(ingredients)
        elif initial == 'exit':
            again = False
        else:
            print('wrong input')

main()
