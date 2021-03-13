import re

variable_dict = {}
result = []
stack = []


def check_command(text: str) -> None:
    if text == "/help":
        print("The program calculates the sum and difference of numbers")
    elif text == "/exit":
        print("Bye!")
        exit()
    else:
        raise AssertionError("Unknown command")


def check_assignment(assignment: list) -> None:
    assert len(assignment) == 3, "Invalid assignment"
    assignment[0] = check_variable(assignment[0])
    if assignment[2].isalpha():
        assignment[2] = return_variable(assignment[2])
    if assignment[2].isdigit():
        variable_dict[assignment[0]] = assignment[2]
    else:
        raise AssertionError("Invalid assignment")


def check_variable(name: str) -> str:
    assert name.isalpha(), "Invalid identifier"
    return name


def format_expression(exp: str) -> str:
    """ Adds spaces around any operators found in a given string, exp """
    for sign in "+-*/^()":
        if sign in exp:
            exp = exp.replace(sign, f" {sign} ")
    return exp


def restore_minus(exp: list, start=0) -> list:
    """ Check if minus is unary minus or subtraction """
    index = exp.index("-", start)
    try:
        if index == 0:
            exp[index + 1] = "-" + exp[index + 1]
            del exp[index]
        elif index != 0:
            if exp[index - 1] in "+-*/^":
                exp[index + 1] = "-" + exp[index + 1]
                del exp[index]
            elif exp[index - 1].isdigit() or exp[index - 1] not in "+-*/^" or exp[index - 1]:
                return restore_minus(exp, index+1)
        return restore_minus(exp)
    except ValueError:
        # print("Returned value: ", exp)
        return exp


def empty_stack(operator: str) -> None:
    # TODO: Adapt for ^ operator
    for op in stack[::-1]:
        if operator in "*/" and op in "+-":
            stack.append(operator)
            break
        elif op == "(":
            stack.pop()
            break
        result.append(stack.pop())


def return_variable(char: str) -> str:
    assert char in variable_dict, "Unknown variable"
    return variable_dict[char]


def cleanup_operators(text: str) -> str:
    if re.search("\*\*+", text) or re.search("\/\/+", text):
        raise AssertionError("Invalid expression")
    if re.search("\+\++", text):
        text = re.sub("\+\++", "+", text)
    if "---" in text:
        text = text.replace("---", "-")
    if "--" in text:
        text = text.replace("--", "+")
    return text


def infix_postfix(calc: list) -> list:
    assert calc.count("(") == calc.count(")"), "Invalid Expression"
    for char in calc:
        # TODO: Adapt for ^ operator
        if char in "+-*/":
            # Add any operator to stack at start or after "("
            if len(stack) == 0 or stack[-1] == "(":
                stack.append(char)
            # If incoming operator has higher precedence than one already in stack
            elif char in "*/" and stack[-1] in "+-":
                stack.append(char)
            # If incoming operator is equal or lower precedence
            else:
                empty_stack(char)
                stack.append(char)
        elif char in "()":
            if char == "(":
                stack.append(char)
            elif char == ")":
                empty_stack(char)
        elif char.isdigit() or char.startswith("-") or char.isalpha():
            result.append(char)
    while stack:
        if stack[-1] in "()":
            stack.pop()
        result.append(stack.pop())
    return result


def calculate(rpn_exp: list) -> int:
    """ Function to take 2 elements from a stack and perform a calculation on them"""
    calc = []
    for i in rpn_exp:
        if i in "+-*/":
            right = calc.pop()
            left = calc.pop()
            if i == "+":
                calc.append(left + right)
            elif i == "-":
                calc.append(left - right)
            elif i == "*":
                calc.append(left * right)
            elif i == "/":
                calc.append(left // right)
            elif i == "^":
                calc.append(left ** right)
        elif i.isdigit() or i.startswith("-"):
            calc.append(int(i))
        elif i.isalpha():
            calc.append(int(return_variable(i)))
    return calc[-1]


def main():
    while True:
        input_str = input()
        try:
            if not input_str:
                continue
            elif input_str.startswith("/"):
                check_command(input_str)
            elif "=" in input_str:
                input_str = input_str.replace("=", " = ")
                check_assignment(input_str.split())
            elif input_str.strip().isalpha():
                print(return_variable(input_str))
            else:
                input_str = format_expression(cleanup_operators(input_str)).split()
                if "-" in input_str:
                    input_str = restore_minus(input_str)
                if len(input_str) == 1:
                    print(int(input_str[0]))
                else:
                    rpn = infix_postfix(input_str)
                    print(calculate(rpn))
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()