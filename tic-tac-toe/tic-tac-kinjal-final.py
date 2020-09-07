def column(rows):
    # output
    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)
    lst = []
    for j in range(rows, 0, -1):
        for i in range(1, rows + 1):
            lst.append([i, j])
    new_list = [''.join(str(elements).strip('[]').replace(',', '')) for elements in lst]
    # print(new_list)
    return new_list


# pretty printing
def print_tic(totalcells, dict1):
    total_step = int(totalcells ** 0.5)
    print('-' * ((total_step * 2) + 3))
    for i in range(0, totalcells, total_step):
        str_tic = ' '.join(list(dict1.values())[i:i + total_step])
        str_tic2 = ' '.join(list(dict1.keys())[i:i + total_step])
        # print(f"| {str_tic} |")
        print(f"| {str_tic} |\t| {str_tic2} |")
    print('-' * ((total_step * 2) + 3))


# pretty printing_structure
def print_tic_struc(totalcells, new_list):
    total_step = int(totalcells ** 0.5)
    for i in range(0, totalcells, total_step):
        str_tic = ' '.join(new_list[i:i + total_step])
        print(f"| {str_tic} |")


def diags(states, diag_step, diag1_step, rows, player, win):
    # check for the diagonals from left to right
    diaglr = len([states[i] for i in range(0, len(states), diag_step) if states[i] == player])

    # check for the diagonals from right to left
    diagrl = len([states[i] for i in range(0, len(states) - 1, diag1_step)[1:] if states[i] == player])

    if (diaglr or diagrl) == rows:
        print(f'{player} won diagonals')
        return player
    else:
        return None


def verticals(states, rows, player, win):
    # check verticals
    # verticals are [0, 3, 6], [1, 4, 7], [2, 5, 8]
    steps = 0
    vert = []
    while steps < rows:
        vertis = len([states[i] for i in range(steps, len(states), rows) if states[i] == player])
        vert.append(vertis)
        steps += 1
    # print(f"The verts are: {vert}")
    if win in vert:
        print(f'{player} won verticals')
        return player
    else:
        return None


def horizon(states, rows, player, win):
    hor = [len(states[i:i + win]) if states[i:i + win] == player * win else 0
           for i in range(0, len(states), rows)]
    # print(f"the hors are {hor}")
    if win in hor:
        print(f'{player} won horizontals')
        return player
    else:
        return None


# impossible
def imp(states):
    # check for impossibles
    count_X = states.count('X')
    count_O = states.count('O')
    sub = abs(count_O - count_X)
    return sub


def game_over(states):
    # game over?
    finish = sum([len(states[i]) for i in range(0, len(states)) if states[i] == '_'])
    return finish


# empty '-'
def empty_cells(total_cells, rows):
    dictO = {}
    value1 = ['-'] * total_cells
    for index in range(total_cells):
        dictO[column(rows)[index]] = str(value1[index])
    print_tic(total_cells, dictO)
    return dictO


# enter state
def tic_tac_cell_state(total_cells, current_player, initial_dict, rows):
    # dict1 = {}
    # value = list(input("Enter cells: "))
    # for index in range(total_cells):
    #     dict1[column(rows)[index]] = str(value[index])
    # print_tic(total_cells, dict1)
    # return dict1

    handle_turn(total_cells, current_player, initial_dict, rows)

    # states for calculating
    states = ''.join(initial_dict.values())
    # print(states)
    return states


# replace 'X' with coordinates, return final_dictionary_state
def handle_turn(total_cells, player, initial_dict, rows):
    # creating a dict for input assignment

    valid = False
    while not valid:
        user_input = input("Enter the coordinates: ")
        if user_input.replace(' ', '').isalpha():
            print("You should enter numbers!")
        elif user_input.replace(' ', '').isdigit():
            out = [int(nums) for nums in user_input.split() if int(nums) > rows]
            if out:
                print(f"Coordinates should be from 1 to {rows}!")
            elif user_input in initial_dict.keys():
                if initial_dict[user_input] != '-':
                    print("This cell is occupied! Choose another one")
                else:
                    valid = True
                    initial_dict[user_input] = player

        print_tic(total_cells, initial_dict)
    return initial_dict


def flip_player(current_player):
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return current_player


# main
def tic_toe():
    rows = 3
    win = 3
    diag_step = rows + 1
    diag1_step = rows - 1
    total_cells = (rows ** 2)

    initial_dict = empty_cells(total_cells, rows)
    current_player = 'X'

    for i in range(total_cells):
        states = tic_tac_cell_state(total_cells, current_player, initial_dict, rows)
        if horizon(states, rows, current_player, win) \
                or verticals(states, rows, current_player, win) \
                or diags(states, diag_step, diag1_step, rows, current_player, win):
            break
        current_player = flip_player(current_player)
    else:
        print("Draw")


tic_toe()
