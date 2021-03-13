# write your code here


# write your code here

def main():
    game = False
    while not game:
        user_input = input()
        if not user_input:
            continue
        elif user_input == '/help':
            print(add_help())
        elif user_input == '/exit':
            print('Bye!')
            break
        elif list(user_input.replace(' ', ''))[0].isdigit() or list(user_input.replace(' ', ''))[1].isdigit():
            text = input_parsing_1(user_input)
            total = text[0]
            working = text[1:]
            for index, elements in enumerate(working):
                if elements == '+':
                    total = add(total, working, index)
                elif elements == '-':
                    total = subtract(total, working, index)
            print(total)
        else:
            print('Invalid Input')


def input_parsing_1(user_input):
    text = [int(num) if num.isdigit()
                        or (num[0] and num[-1].isdigit())
            else num
            for num in user_input.split()]
    for i, elements in enumerate(text):
        if type(elements) == type(""):
            if '-' in elements and len(elements) % 2 == 0 or '+' in elements:
                text[i] = '+'
            else:
                text[i] = '-'
    return text


def input_parsing(user_input):
    # trying = ''.join(list(user_input.replace(' ', '')))
    # print(trying)
    text = [int(num) if num.isdigit()
                        or (num[0] and num[-1].isdigit())
            else ''.join(set(num))
            for num in user_input.split()]
    return text


def add(total, working, index):
    total += working[index + 1]
    return total

    # return sum(list(map(int, n)))


def subtract(total, working, index):
    total -= working[index + 1]
    return total


def add_help():
    return """The program calculates does basic addition and subtraction. 
    Separate each number/sign with a space like: 5 + 8 - 2.
    Type '/exit' to exit."""


main()
