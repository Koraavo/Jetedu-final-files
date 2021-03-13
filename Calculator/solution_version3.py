while True:
    n = input()
    if n == "/exit":
        print("bye!")
        exit()
    elif n == "/help":
        print("use + = The program calculates the sum of numbers\n"
              "use - = The program calculates the subtraction of numbers")
    elif len(n) != 0 and " " not in n and "/" not in n:
        try:
            y = int(n)
            print(y)
        except ValueError:
            print('Invalid expression')
    elif len(n) > 1 and " " in n and "+" not in n and "-" not in n:
        print("Invalid expression")
    elif len(n) > 1 and "+" in n or "-" in n:
        try:
            if '---' in n:
                n = n.replace("---", "-")
            if '--' in n:
                n = n.replace("--", "+")
            if '- ' in n:
                n = n.replace("- ", "-")
            if '+' in n:
                n = n.replace("+", "")
            s = 0
            y = n.split()
            for i in y:
                s += int(i)
            print(s)
        except ValueError:
            print('Invalid expression')
    elif n == "":
        pass
    else:
        print('Unknown command')