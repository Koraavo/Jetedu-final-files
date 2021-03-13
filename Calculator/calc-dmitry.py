from collections import deque
import re

variables = {}
oper_precedence = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}


def is_operator(value: str):
    return value in "-+/*^"


def is_numeric(value: str):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_sign(value: str):
    return "-" if value.count("-") % 2 else ""


def calc(operator, left_operand, right_operand):
    left = int(left_operand)
    right = int(right_operand)
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        return left // right
    elif operator == '^':
        return left ** right


def calculate_rpn_expr(rpn_expr):
    stack = deque()
    for elem in rpn_expr:
        if is_numeric(elem):
            stack.append(elem)
        else:
            right_operand, left_operand = stack.pop(), stack.pop()
            stack.append(calc(elem, left_operand, right_operand))
    return stack.pop()


def assign(expr: str):
    name, value = (val.strip() for val in expr.split('=', 1))
    if not name.isalpha():
        print("Invalid identifier")
    elif not is_numeric(value):
        if value in variables:
            variables[name] = variables[value]
        else:
            print("Invalid assignment")
    else:
        variables[name] = value


def tokenize(expr):
    tokens = []

    current_token = expr[0]
    sign = ""
    for value in expr[1:]:
        if current_token in "()*/^+":
            tokens.append(current_token)
            current_token = value
        elif current_token.isalpha():
            if value.isalpha():
                current_token += value
            elif is_operator(value):
                tokens.append(current_token)
                current_token = value
        elif is_numeric(current_token):
            if is_numeric(value):
                current_token += value
            else:
                tokens.append(sign + current_token)
                sign = ""
                current_token = value
        elif "-" in current_token:
            if value == "-" or not tokens:
                current_token += value
            elif is_numeric(value) or value == "(" or value.isalpha():
                if tokens[-1] in "+*/^":
                    sign = get_sign(current_token)
                    current_token = value
                elif is_numeric(tokens[-1]) or tokens[-1] == ")" or tokens[-1].isalpha():
                    tokens.append(current_token[0])
                    current_token = value

    tokens.append(current_token)
    return tokens


def to_rpn_expr(tokenized_expr):
    rpn_expr = []
    stack = deque()

    for token in tokenized_expr:
        if token.isalpha():
            if token in variables:
                rpn_expr.append(int(variables[token]))
            else:
                raise NameError
        elif is_numeric(token):
            rpn_expr.append(int(token))
        elif is_operator(token):
            if not stack or stack[-1] == "(":
                stack.append(token)
            elif oper_precedence[token] > oper_precedence[stack[-1]]:
                stack.append(token)
            else:
                while stack and stack[-1] != "(" and oper_precedence[stack[-1]] >= oper_precedence[token]:
                    rpn_expr.append(stack.pop())
                stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                rpn_expr.append(stack.pop())
            else:
                stack.pop()

    while stack:
        rpn_expr.append(stack.pop())

    return rpn_expr


def sanitize(expr: str):
    expr = re.sub(r"\++", "+", expr)
    return expr.replace(" ", "")


def evaluate(expr: str):
    try:
        expr = sanitize(expr)
        rpn_expr = to_rpn_expr(tokenize(expr))
        print(calculate_rpn_expr(rpn_expr))
    except NameError:
        print("Unknown variable")
    except Exception:
        print("Invalid expression")


while True:
    expression = input()
    if expression:
        if '=' in expression:
            assign(expression)
        elif expression.startswith("/"):
            if expression == "/exit":
                print("Bye!")
                break
            elif expression == "/help":
                print("Simple calculator, supports basic operations(+,-,/,*,^) and variables")
            else:
                print("Unknown command")
        else:
            evaluate(expression)