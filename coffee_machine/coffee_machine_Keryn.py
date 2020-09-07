class CoffeeMachine:
    class_descriptor = "a class that represents a coffee machine... when user inputs string to console," \
        "the program invokes a method with just that one argument... the class does not" \
        "use system input at all; it only handles the input that comes via the method and its" \
        "single argument... works by storing the current state to work out how to interpret" \
        "the user input."

    solved_by = "1. create a an input handler method that returns the input, " \
                "and takes the current state as its argument" \
                "2. any other method calls the input handler any time user input is" \
                "required, and takes the input as its argument."

    # define class lists (enables easily adding further coffee types or options, without having to alter the methods)
    option_name = ["espresso,", "latte,", "cappuccino,"]
    option_water = [250, 350, 200]
    option_milk = [0, 75, 100]
    option_beans = [16, 20, 12]
    option_cost = [4, 7, 6]

    # define class methods
    def __init__(self):
        # starting values, as specified in problem statement
        self.water_has = 400
        self.milk_has = 540
        self.beans_has = 120
        self.cups_has = 9
        self.money_has = 550

        # initiate input handler
        self.input_handler("choosing an action")

    def input_handler(self, state):
        if state == "choosing an action":
            print("Write  action (buy, fill, take, remaining, exit):")
        elif state == "choosing a type of coffee":
            print("What do you want to buy? 1 -", CoffeeMachine.option_name[0], "2 -", CoffeeMachine.option_name[1],
                  "3 -", CoffeeMachine.option_name[2], "back - to main menu:")
        elif state == "adding water":
            print("Write how many ml of water do you want to add:")
        elif state == "adding milk":
            print("Write how many ml of milk do you want to add:")
        elif state == "adding beans":
            print("Write how many grams of coffee beans do you want to add:")
        elif state == "adding cups":
            print("Write how many disposable cups do you want to add:")
        self.action_handler(state, input())

    def action_handler(self, state, action):
        # main menu actions
        if state == "choosing an action":
            # user selects "exit" from main menu
            if action == "exit":
                pass
            # user selects "take" from main menu
            elif action == "take":
                print("I gave you $", self.money_has)
                self.money_has = 0
                self.input_handler(state)
                # user selects "remaining" from main menu
            elif action == "remaining":
                print("The coffee machine has:")
                print(self.water_has, "of water")
                print(self.milk_has, "of milk")
                print(self.beans_has, "of coffee beans")
                print(self.cups_has, "of disposable cups")
                print("$", self.money_has, "of money")
                self.input_handler(state)
            # user selects "fill" from main menu
            elif action == "fill":
                state = "adding water"
                self.input_handler(state)
            # user selects "buy" from main menu
            elif action == "buy":
                state = "choosing a type of coffee"
                self.input_handler(state)
            # user entry is not a valid main menu option, or action is Null
            else:
                self.input_handler(state)
        # fill actions (after: user has selected "fill" from main menu)
        elif state == "adding water":
            self.water_has += int(action)
            state = "adding milk"
            self.input_handler(state)
        elif state == "adding milk":
            self.milk_has += int(action)
            state = "adding beans"
            self.input_handler(state)
        elif state == "adding beans":
            self.beans_has += int(action)
            state = "adding cups"
            self.input_handler(state)
        elif state == "adding cups":
            self.cups_has += int(action)
            state = "choosing an action"
            self.input_handler(state)
        # buy actions (after: user has selected "buy" from main menu)
        elif state == "choosing a type of coffee":
            # user selects "back" from the "buy" menu
            if action == "back":
                state = "choosing an action"
                self.input_handler(state)
            # user selects coffee option from the "buy" menu
            elif action in ("1", "2", "3"):
                # not-enough-materials-to-make-coffee actions
                not_enough = ("water!" if self.option_water[int(action) - 1] >= self.water_has
                              else "milk!" if self.option_milk[int(action) - 1] >= self.milk_has
                              else "beans!" if self.option_beans[int(action) - 1] >= self.beans_has
                              else "cups!" if self.cups_has == 0
                              else "has_enough")
                if not_enough != "has_enough":
                    print("Sorry, not enough", not_enough)
                    state = "choosing an action"
                    self.input_handler(state)
                # enough-materials actions (making coffee)
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water_has -= self.option_water[int(action) - 1]
                    self.milk_has -= self.option_milk[int(action) - 1]
                    self.beans_has -= self.option_beans[int(action) - 1]
                    self.cups_has -= 1
                    self.money_has += self.option_cost[int(action) - 1]
                    state = "choosing an action"
                    self.input_handler(state)
            # user entry is not a valid "buy" menu option, or action is Null
            else:
                self.input_handler(state)

CoffeeMachine()
