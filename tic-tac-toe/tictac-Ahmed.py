word = input("Enter cells:")
cell_list = []
x_found_in = []
o_found_in = []
i = 0
for cell in word:
    cell_list.append(cell)

M = [[cell_list[0], cell_list[1], cell_list[2]], [cell_list[3], cell_list[4], cell_list[5]],
     [cell_list[6], cell_list[7], cell_list[8]]]
print("---------")
print("| " + M[0][0] + " " + M[0][1] + " " + M[0][2] + " |")
print("| " + M[1][0] + " " + M[1][1] + " " + M[1][2] + " |")
print("| " + M[2][0] + " " + M[2][1] + " " + M[2][2] + " |")
print("---------")


def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True


found = False

while not found:
    p1, p2 = input().split()
    if is_int(p1) and is_int(p2):
        p1 = int(p1)
        p2 = int(p2)
        if p1 <= 3 and p2 <= 3:
            if M[3 - p2][p1 - 1] == 'X' or M[3 - p2][p1 - 1] == 'O':
                found = False
                print("This cell is occupied! Choose another one!")
            else:
                M[3 - p2][p1 - 1] = 'X'
                found = True
        else:
            found = False
            print("Coordinates should be from 1 to 3!")

    else:
        print("You should enter numbers!")

print("---------")
print("| " + M[0][0] + " " + M[0][1] + " " + M[0][2] + " |")
print("| " + M[1][0] + " " + M[1][1] + " " + M[1][2] + " |")
print("| " + M[2][0] + " " + M[2][1] + " " + M[2][2] + " |")
print("---------")