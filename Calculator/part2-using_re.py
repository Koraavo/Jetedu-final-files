# write your code here
import re


VARIABLES = dict()


class InvalidIdentifier(Exception):
    def __str__(self):
        return "Invalid identifier"


class UnknownVariable(Exception):
    def __str__(self):
        return "Unknown variable"


class InvalidAssignment(Exception):
    def __str__(self):
        return "Invalid assignment"


def check_valid_variable(x):
    ascii_pat = '^[a-zA-Z]+$'
    return re.match(ascii_pat, x.strip()) is not None


def check_value(x):
    x = x.strip()
    return x.isdigit() or (x in VARIABLES) or check_valid_variable(x)


def check_assignment(inp):
    assign_pat = r'(?P<variable>[\w\s]+)=(?P<value>[\w\s=]+)'
    m = re.search(assign_pat, inp)
    if m:
        variable = m.group('variable')
        value = m.group('value')
        if not check_valid_variable(variable):
            raise InvalidIdentifier
        if not check_value(value):
            raise InvalidAssignment
        return True
    return False



def main():
    while True:
        inp = input()
        try:
            if inp == '/exit':
                print("Bye!")
                break
            elif inp == '/help':
                print('The program calculates the sum/subtract of numbers')
            elif inp.startswith('/'):
                print("Unknown command")
            elif not inp:
                continue
            elif inp.strip() in VARIABLES:
                print(VARIABLES[inp.strip()])
            elif check_assignment(inp):
                exec(inp)
            else:
                result = eval(inp)
                print(result)
        except NameError:
            print(UnknownVariable())
        except InvalidAssignment:
            print(InvalidAssignment())
        except InvalidIdentifier:
            print(InvalidIdentifier())
        except:
            print("Invalid expression")


if __name__ == '__main__':
    main()