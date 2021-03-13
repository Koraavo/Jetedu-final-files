# write your code here

import sys
from collections import deque


def equal(user_input, dict_input) -> dict:
    """Check if there is an assignment and create a dictionary with the assignments"""
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


def bracker_checker(string_input):
    stack = deque()
    p1 = ['(', ')']
    for elements in list(string_input.strip()):
        if elements == p1[0]:
            stack.append(elements)
        elif elements == p1[1]:
            if stack:
                stack.pop()
            else:
                return 'ERROR'
    if stack:
        return 'ERROR'
    else:
        return 'OK'


def handling_initial_inputs(user_input) -> str:
    """Handling user-inputs with + and -"""
    out = ''.join(user_input.split())
    if '**' in out:
        return 'Invalid expression'
    else:
        while '++' in out:
            out = out.replace('++', '+')
        while '---' in out:
            out = out.replace('---', '-')
        while '--' in out:
            out = out.replace('--', '+')
        return out


def check_inputs(initial_input, equals):
    for elements in initial_input:
        if elements not in equals and elements not in ('+-*/()') \
                and not elements.isdigit():
            return 'Unknown Variable'


def dealing_with_variables(initial_inputs, equals, dict_input) -> str:
    """If variables exist in user_inputs,
    check in the dictionary
    Unknown Variable, if elements not numbers or variables or operators
    else
    create a str with the values of the variables, numbers and operators
    """
    parsed_input = ''
    for elements in initial_inputs:
        if elements in equals:
            value = str(dict_input[elements])
            parsed_input += value
        else:
            value = elements
            parsed_input += value
    return parsed_input


def spaced_inputs(out) -> str:
    """Spacing the output with the operators to use it for creating a postfix algo"""
    if '+' in out:
        out = out.replace('+', ' + ')
    if '-' in out[1:]:
        out = out[0] + out[1:].replace('-', ' - ')
    if '*' in out:
        out = out.replace('*', ' * ')
    if '//' in out:
        out = out.replace('//', ' // ')
    elif '/' in out:
        out = out.replace('/', ' / ')
    if '(' in out:
        out = out.replace('(', ' ( ')
    if ')' in out:
        out = out.replace(')', ' ) ')
    else:
        out = out
    out = out.replace('  ', ' ')
    return out


def handling_minus(out):
    if ' - ' in out[1:]:
        if out[out.index(' - ')-1] == '*' or out[out.index(' - ')-1] == '/' or out[out.index(' - ')-1] == '+' or out[out.index(' - ')-1] == '-':
            try:
                out = out.replace(' - ', ' -')
            except:
                out = out
    return out


def post_fix(string_input) -> list:
    """Create a postfix algo"""
    pri = {}
    pri['('] = 3
    pri['*'] = 2
    pri['/'] = 2
    pri['//'] = 2
    pri['+'] = 1
    pri['-'] = 1

    opstack = deque()
    postfix = []
    for elements in string_input.split():
        if elements.lstrip('+-').isdigit() or elements.isalpha():
            # Add operands (numbers and variables) to the result (postfix notation) as they arrive.
            postfix.append(elements)

        elif not opstack or opstack[-1] == '(' or elements == '(':
            # If the stack is empty or contains a left parenthesis on top, push the incoming operator on the stack.
            # If the incoming element is a left parenthesis, push it on the stack.
            opstack.append(elements)
        elif elements == ')':
            # If the incoming element is a right parenthesis,
            # pop the stack and add operators to the result
            # until you see a left parenthesis.
            while opstack[-1] != '(':
                token = opstack.pop()
                postfix.append(token)
            # Discard the pair of parentheses.
            opstack.remove('(')
        else:
            while len(opstack) != 0 and pri[elements] <= pri[opstack[-1]] and opstack[-1] != '(':
                # If the precedence of the incoming operator is
                # lower than or equal to that of the top of the stack,
                # pop the stack and add operators to the result
                # until you see an operator that has smaller precedence
                # or a left parenthesis on the top of the stack;
                # then add the incoming operator to the stack.
                token = opstack.pop()
                postfix.append(token)
            opstack.append(elements)

    while opstack:
        # At the end of the expression, pop the stack and add all operators to the result.
        postfix.append(opstack.pop())
    return postfix


def eval_postfix(list_input):
    """Evaluate the postfix algo"""
    operands = []
    if len(list_input) == 1 and '-' not in list_input[0][1:]:
        return list_input[0]
    elif len(list_input) == 1 and '-' in list_input[0][1:]:
        operand1 = int(list_input[0][:list_input[0].index('-', 1)])
        operand2 = int(list_input[0][list_input[0].index('-', 1):])
        operand = '+'
        result = doMath(operand, operand2, operand1)
        operands.append(result)
        return operands.pop()
    elif len(list_input) == 2:
        for elements in list_input:
            if elements.lstrip('+-').isdigit() or elements.isalpha():
                operands.append(elements)
        operand1 = int(operands.pop())
        operand2 = int(operands.pop())
        operand = '+'
        result = doMath(operand, operand2, operand1)
        operands.append(result)
        return operands.pop()
    else:
        for elements in list_input:
            if elements.lstrip('+-').isdigit() or elements.isalpha():
                operands.append(elements)
            else:
                operand1 = int(operands.pop())
                operand2 = int(operands.pop())
                operand = elements
                result = doMath(operand, operand2, operand1)
                operands.append(result)
        return operands.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "//":
        return int(op1 / op2)
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def help_exit(user_input):
    if user_input == '/help':
        return """The program does basic calculations as per the BODMAS Rule:
Separate each number/sign with a space like: 5 + 8 - 2. 
If there are multiple '-' and they are even, then it adds the number,
else it performs a subtraction. Type '/exit' to exit."""
    elif user_input == '/exit':
        print('Bye!')
        sys.exit()
    elif user_input[0].startswith('/'):
        return 'Unknown Command'


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
        elif bracker_checker(user_input) == 'ERROR':
            print('Invalid expression')
        else:
            initial_input = handling_initial_inputs(user_input)
            equals = equal(user_input, dict_input)
            if initial_input == 'Invalid expression':
                print('Invalid expression')
            elif check_inputs(initial_input, equals) == 'Unknown Variable':
                print('Unknown Variable')
            else:
                parsed_input = dealing_with_variables(initial_input, equals, dict_input)
                # print(parsed_input)
                out = spaced_inputs(parsed_input)
                # print(out)
                new_output = handling_minus(out)
                print(new_output)
                eval_for_postfix = post_fix(new_output)
                print(eval_for_postfix)
                print(eval_postfix(eval_for_postfix))



main()
# print(handling_minus('33 + 20 + 11 + 49 - 32 - 9 + 1 - 80 + 4'))
# a * 4 / b - (3 - 1)
# print(handling_minus('-10 * - 2'))