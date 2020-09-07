# Write your code here
water_machine = int(input("Write how many ml of water the coffee machine has: "))
milk_machine = int(input("Write how many ml of milk the coffee machine has: "))
beans_machine = int(input("Write how many grams of coffee beans the coffee machine has: "))
coffee_cups = int(input("Write how many cups of coffee you will need: "))
# print("For 25 cups of coffee you will need: ")

# water = coffee_cups * 200
# milk = coffee_cups * 50
# coffee_beans = coffee_cups * 15

poss_water = int(water_machine / 200)
poss_milk = int(milk_machine / 50)
poss_beans = int(beans_machine / 15)

poss_coffee = min(poss_water, poss_milk, poss_beans)
if coffee_cups == poss_coffee:
    print("Yes, I can make that amount of coffee")
elif coffee_cups > poss_coffee:
    print("No, I can make only", poss_coffee, "cups of coffee")
elif coffee_cups < poss_coffee:
    print("Yes, I can make that amount of coffee (and even", poss_coffee-coffee_cups, "more than that)")