
from collections import deque

def bracker_checker(string_input):
    stack = deque()
    p1 = ['(', ')']
    for elements in list(string_input.strip()):
        if elements == p1[0]:
            stack.append(elements)
        elif elements == ')':
            if stack:
                stack.pop()
            else:
                return 'ERROR'
    if stack:
        return 'ERROR'
    else:
        return 'OK'


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = deque()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while opStack and \
               (prec[opStack[-1]] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.append(token)

    while opStack:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

# 3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)
# 3 8 4 3 + 2 * 1 + * + 6 2 1 + / -


def postfixEval(postfixExpr):
    operandStack = []
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.append(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.append(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

# print(infixToPostfix('33 + 20 + 11 + 49 - 32 - 9 + 1 - 80 + 4'))

print(bracker_checker('8 * 3 + 12 * (4 - 2)'))