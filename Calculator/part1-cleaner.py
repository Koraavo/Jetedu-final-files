# write your code here


# write your code here
import sys


def main():
    game = False
    while not game:
        user_input = input().split()
        if not user_input:
            continue
        elif user_input[0] == '/help':
            print(add_help())
        elif user_input[0] == '/exit':
            print('Bye!')
            sys.exit()
        elif user_input[0].startswith('/') and user_input[0][1:].isalpha():
            print('Unknown command')
        elif user_input:
            invalid = False
            operators_list = ['+', '-', '/', '*']
            numbers = []
            operators = []
            # print(user_input)
            for i, elements in enumerate(user_input):
                if i % 2 == 0 and elements.lstrip('+-').isnumeric():
                    numbers.append(int(elements))
                elif i % 2 == 1 and len(user_input) > 1:
                    for operator in operators_list:
                        if operator in elements:
                            operators.append(elements)
                else:
                    invalid = True

            if (not operators and len(user_input) > 1) or (operators and len(numbers) < 2):
                # print(numbers, operators)
                invalid = True
            # print(numbers, operators)
            if invalid:
                print("Invalid expression")
            else:
                print(operator_influx(numbers, operators))


# annotation saying the output will return an integer
def operator_influx(numbers, operators) -> int:
    total = numbers[0]
    numbers = numbers[1:]
    for number, operator in zip(numbers, operators):
        # print(number, operator)
        if '+' in operator:
            total += number
        elif '-' in operator:
            if len(operator) % 2 == 0:
                total += number
            else:
                total -= number
        elif '*' in operator:
            total *= number
        elif '/' in operator:
            total /= number
    return total


def add_help():
    return """The program does basic addition and subtraction:
    Separate each number/sign with a space like: 5 + 8 - 2.
    if there are multiple '-' and they are even, then it adds the number,
    else it performs a subtraction.
    Type '/exit' to exit."""


main()