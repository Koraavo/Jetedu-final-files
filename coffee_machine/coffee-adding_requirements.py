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
