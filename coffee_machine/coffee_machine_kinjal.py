# # Write your code here
class CoffeeMachine:

    # initiating given requirements
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.coffee_cups = 9
        self.money = 550
        self.again = True

        # creating a dict of the ingredients
        self.ingredients = {'water': self.water, 'milk': self.milk, 'coffee_beans': self.coffee_beans,
                            'coffee_cups': self.coffee_cups, 'money': self.money}

        # initiating the question
        self.question()

    def question(self):
        # flag check
        while self.again:
            # action requested
            ask = input("Write action (buy, fill, take, remaining, exit): ")
            if ask == 'buy':
                self.buy()
            elif ask == 'fill':
                self.fill()
            elif ask == 'take':
                self.take()
            elif ask == 'remaining':
                self.remaining()
            elif ask == 'exit':
                self.again = False
            else:
                print('wrong input')


    def print_actions(self):
        print(f"""
            The coffee machine has:
            {self.ingredients['water']} of water
            {self.ingredients['milk']} of milk
            {self.ingredients['coffee_beans']} of coffee beans
            {self.ingredients['coffee_cups']} of disposable cups
            ${self.ingredients['money']} of money
            """)


    def enough(self, requirements):
        # check if each ingredients match the requirement and then add/sub
        if self.ingredients['water'] >= requirements['water']:
            if self.ingredients['milk'] >= requirements['milk']:
                if self.ingredients['coffee_beans'] >= requirements['coffee_beans']:
                    if self.ingredients['coffee_cups'] >= requirements['coffee_cups']:
                        print('I have enough resources, making you a coffee!')
                        self.ingredients['water'] -= requirements['water']
                        self.ingredients['milk'] -= requirements['milk']
                        self.ingredients['coffee_beans'] -= requirements['coffee_beans']
                        self.ingredients['coffee_cups'] -= requirements['coffee_cups']
                        self.ingredients['money'] += requirements['money']
                    else:
                        print('Sorry, not enough cups!')
                else:
                    print('Sorry, not enough beans!')
            else:
                print('Sorry, not enough milk!')
        else:
            print('Sorry, not enough water!')

        return self.ingredients

    def buy(self):
        what = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if what == '1':
            requirements = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'coffee_cups': 1, 'money': 4}
            self.enough(requirements)

        elif what == '2':
            requirements = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'coffee_cups': 1, 'money': 7}
            self.enough(requirements)

        elif what == '3':
            requirements = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'coffee_cups': 1, 'money': 6}
            self.enough(requirements)

        elif what == 'back':
            self.question()

    def fill(self):
        self.ingredients['water'] += int(input("Write how many ml of water do you want to add: "))
        self.ingredients['milk'] += int(input("Write how many ml of milk do you want to add: "))
        self.ingredients['coffee_beans'] += int(input("Write how many grams of coffee beans do you want to add: "))
        self.ingredients['coffee_cups'] += int(input("Write how many disposable cups of coffee do you want to add: "))

    def take(self):
        print("I gave you", self.ingredients['money'])
        self.ingredients['money'] = 0

    def remaining(self):
        self.print_actions()


CoffeeMachine()
