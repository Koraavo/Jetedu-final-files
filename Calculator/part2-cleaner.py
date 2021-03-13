# write your code here


# write your code here
import sys


def main():
    game = False
    dict_input = {}
    while not game:
        user_input = input()
        if not user_input:
            pass
        elif help_exit(user_input):
            print(help_exit(user_input))
        elif '=' in user_input:
            equal(user_input, dict_input)
        else:
            user_input = user_input.split()
            numbers, operator_list = operators(user_input)
            # print(operators(user_input))
            print(calculations(operator_list, dict_input, numbers))


def handling_inputs(user_input):
    out = ''.join(user_input.split())
    while '++' in out:
        out = out.replace('++', '+')
    while '---' in out:
        out = out.replace('---', '-')
    while '--' in out:
        out = out.replace('--', '+')
    else:
        out = out

    if '+' in out:
        out = out.replace('+', ' + ')
    if '-' in out:
        out = out.replace('-', ' - ')
    if '*' in out:
        out = out.replace('*', ' * ')
    if '/' in out:
        out = out.replace('/', ' / ')
    if out == '(':
        out = out.replace('(', ' ( ')
    if out == ')':
        out = out.replace(')', ' ) ')
    return out


def operators(user_input):
    numbers = []
    operator_list = []
    for i, values in enumerate(user_input):
        if i % 2 == 1 and len(user_input) > 1:
            operator_list.append(values)
        elif i % 2 == 0 and values.lstrip('+-'):
            numbers.append(values)
    return numbers, operator_list


def calculations(operator_list, dict_input, numbers):
    values = []
    for each_number in numbers:
        if each_number in dict_input.keys():
            values.append(dict_input[each_number])
        elif each_number.isdigit():
            values.append(int(each_number))
        else:
            if each_number.startswith('/'):
                return help_exit(values)
            else:
                return 'Unknown Variable'
    total = values[0]
    values = values[1:]
    for number, operator in zip(values, operator_list):
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


def equal(user_input, dict_input):
    if '=' in user_input:
        user_input = [user.strip() for user in user_input.split('=')]
        if user_input[0].isalpha():
            if user_input[1].isdigit():
                dict_input[user_input[0]] = int(user_input[1])
            elif user_input[1] in dict_input.keys():
                dict_input[user_input[0]] = int(dict_input[user_input[1]])
            else:
                print("Invalid assignment")
        else:
            print("Invalid identifier")
    return dict_input


def help_exit(user_input):
    if user_input == '/help':
        return """The program does basic addition and subtraction:
        Separate each number/sign with a space like: 5 + 8 - 2.
        if there are multiple '-' and they are even, then it adds the number,
        else it performs a subtraction.
        Type '/exit' to exit."""
    elif user_input == '/exit':
        print('Bye!')
        sys.exit()
    elif user_input[0].startswith('/'):
        return 'Unknown Command'


main()
