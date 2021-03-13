# write your code here


# write your code here
import sys


def main():
    game = False
    invalid = False
    # creating a dict of elements with their respective assignments
    dict_inputs = {}
    while not game and not invalid:
        operators_list = ['+', '-', '/', '*']
        # while operators_list not in user_input:
        user_input = input()
        if '=' in user_input:
            user_input = [user.strip() for user in user_input.split('=')]
            user_input.append('=')
            if user_input[0].isalpha():
                if user_input[1].isdigit():
                    dict_inputs[user_input[0]] = int(user_input[1])
                elif user_input[1] in dict_inputs.keys():
                    dict_inputs[user_input[0]] = int(dict_inputs[user_input[1]])
                else:
                    print("Invalid assignment")
            else:
                print("Invalid identifier")
            print(dict_inputs)
        else:
            user_input = user_input.split()

        if not user_input:
            continue
        elif user_input[0] == '/help':
            print(add_help())
        elif user_input[0] == '/exit':
            print('Bye!')
            sys.exit()
        elif user_input[0].startswith('/') and user_input[0][1:].isalpha():
            print('Unknown command')
        else:
            numbers = []
            operators = []
            # print(user_input)
            for i, elements in enumerate(user_input):
                if i % 2 == 0 and elements.lstrip('+-'):
                    numbers.append(elements)
                elif i % 2 == 1 and len(user_input) > 1:
                    for operator in operators_list:
                        if operator in elements:
                            operators.append(elements)
                else:
                    invalid = True

            if '=' in user_input:
                pass
            else:
                if (not operators and len(user_input) > 1) or (operators and len(numbers) < 2):
                    # print(numbers, operators)
                    invalid = True
                print(numbers, operators)

            if invalid:
                print("Invalid expression")
            else:
                if '=' not in user_input:
                    print(operator_influx(numbers, operators, dict_inputs))


# annotation saying the output will return an integer
def operator_influx(numbers, operators, dict_inputs) -> [str, int]:
    values = []
    for each_number in numbers:
        if each_number in dict_inputs.keys():
            values.append(dict_inputs[each_number])
        elif each_number.isdigit():
            values.append(int(each_number))
        else:
            return 'Unknown Variable'
    total = values[0]
    values = values[1:]
    for number, operator in zip(values, operators):
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
