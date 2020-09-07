def print_actions(water, milk, coffee_beans, coffee_cups, money):
    print(f"""
    The coffee machine has:
    {water} of water
    {milk} of milk
    {coffee_beans} of coffee beans
    {coffee_cups} of disposable cups
    {money} of money
    """)


def action(x):
    water = 400
    milk = 540
    coffee_beans = 120
    coffee_cups = 9
    money = 550

    if x == 'buy':
        question = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
        if question == 1:
            water -= 250
            coffee_beans -= 16
            coffee_cups -= 1
            money += 4

            print_actions(water, milk, coffee_beans, coffee_cups, money)

        elif question == 2:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            coffee_cups -= 1
            money += 7

            print_actions(water, milk, coffee_beans, coffee_cups, money)

        elif question == 3:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            coffee_cups -= 1
            money += 6

            print_actions(water, milk, coffee_beans, coffee_cups, money)

    elif x == 'fill':
        water_ques = input("Write how many ml of water do you want to add: ")
        milk_ques = input("Write how many ml of milk do you want to add: ")
        beans_ques = input("Write how many grams of coffee beans do you want to add: ")
        cups_ques = input("Write how many disposable cups of coffee do you want to add: ")
        water += int(water_ques)
        milk += int(milk_ques)
        coffee_beans += int(beans_ques)
        coffee_cups += int(cups_ques)

        print_actions(water, milk, coffee_beans, coffee_cups, money)

    elif x == 'take':

        print("I gave you", money)
        print(f"""
                The coffee machine has:
                {water} of water
                {milk} of milk
                {coffee_beans} of coffee beans
                {coffee_cups} of disposable cups
                {money-money} of money
                """)


print_actions(water=400, milk=540, coffee_beans=120, coffee_cups=9, money=550)
x = input("Write action (buy, fill, take):> ")
action(x)
