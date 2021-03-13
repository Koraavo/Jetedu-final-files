def eval_(args: [str]):
    if not args:
        return 0

    elif len(args) == 1 and not args[0].lstrip("-+").isnumeric():
        return 0

    else:
        if args[0].lstrip("-+").isnumeric():
            return int(args[0].lstrip("-+")) * (-1) ** args[0].count("-") + eval_(args[1:])

        else:
            return eval_([args[0] + args[1]] + args[2:])


while 1:
    inp = input()
    if inp == "/help":
        print("some information about the program.")

    elif inp == "/exit":
        break

    elif inp:
        print(eval_(inp.split()))

print("Bye!")