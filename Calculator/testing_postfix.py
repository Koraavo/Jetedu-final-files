from collections import deque


def post_fix(string_input) -> list:
    """Create a postfix algo"""
    pri = {}
    pri['('] = 3
    pri['*'] = 2
    pri['/'] = 2
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
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(post_fix('33 + 20 + 11 + 49 - 32 - 9 + 1 - 80 + 4'))
print(post_fix('33 + 20 + 11 + 49 + -32 + -9 + 1 + -80 + 4'))
print(eval_postfix(['33', '20', '+', '11', '+', '49', '+', '-32', '+', '-9', '+', '1', '+', '-80', '+', '4', '+']))