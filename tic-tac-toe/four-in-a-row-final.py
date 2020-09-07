def column(rows):
    # output
    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)
    # ['1 3', '2 3', '3 3', '1 2', '2 2', '3 2', '1 1', '2 1', '3 1']
    # lst = []
    # for j in range(rows, 0, -1):
    #     for i in range(1, rows + 1):
    #         lst.append([i, j])
    lst = [i for i in range(rows ** 2)]
    new_list = [''.join(str(elements).strip('[]').replace(',', '').zfill(2)) for elements in lst]
    return new_list


# pretty printing
def print_tic(totalcells, dict1):
    total_step = int(totalcells ** 0.5)
    print('-' * ((total_step * 2) + 3))
    for i in range(0, totalcells, total_step):
        str_tic = ' '.join(list(dict1.values())[i:i + total_step])
        str_tic2 = ' '.join(list(dict1.keys())[i:i + total_step])
        # print(f"| {str_tic} |")
        print(f"| {str_tic} |\t{str_tic2}")
    print('-' * ((total_step * 2) + 3))


def which_vertical(states, rows):
    # check verticals
    # verticals are [0, 3, 6], [1, 4, 7], [2, 5, 8]
    steps = 0
    vert = []
    while steps < rows:
        vertis = [str(i).zfill(2) for i in range(steps, len(states), rows)]
        vert.append(vertis)
        steps += 1
    return vert


def diags(states, diag_step_lr, diag_step_rl, rows, slice, step1, step2, step3, step4, player, win):
    sec_list = []
    while step1 < rows:
        # range(0, 49, 8)[0:7]
        # left to right (+)
        # slice -= 1 ergo [0:6], [0:5] and so on
        diag1 = ([str(i).zfill(2) for i in range(step1, len(states), diag_step_lr)][0:slice])
        # range(7, 49, 8)
        diag2 = [str(i).zfill(2) for i in range(step2, len(states), diag_step_lr)[0:slice]]

        # range(6, 49, 6)[0:7]
        # right to left (-)
        diag3 = ([str(i).zfill(2) for i in range(step3, len(states), diag_step_rl)][0:slice])
        # range(13, 49, 6)[0:7]
        diag4 = [str(i).zfill(2) for i in range(step4, len(states), diag_step_rl)[0:slice]]

        step1 += 1
        step2 += rows
        step3 -= 1
        step4 += rows
        slice -= 1
        if diag1:
            sec_list.append(diag1)
        if diag2:
            sec_list.append(diag2)
        if diag3:
            sec_list.append(diag3)
        if diag4:
            sec_list.append(diag4)
    # print(sec_list)

    num_of_elements = []
    for i, j in enumerate(sec_list):
        if str(states.index(player)).zfill(2) in j:
            num = [ele for ele in j if states[int(ele)] == player]
            num_of_elements.append(len(num))
    # print(num_of_elements)

    if win in num_of_elements:
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
    if win in vert:
        print(f'{player} won verticals')
        return player
    else:
        return None


def horizon(states, rows, player, win):
    for i in range(0, len(states), rows):
        # if index of player = 42
        # states[42:46] == player * 4
        if states[states.index(player):states.index(player) + win] == player * win:
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
    handle_turn(total_cells, current_player, initial_dict, rows)

    # states for calculating
    states = ''.join(initial_dict.values())
    # print(states)
    return states


# replace 'X' with coordinates, return final_dictionary_state
# in case the values are coordinates, else regular numbers
def handle_turn(total_cells, player, initial_dict, rows):
    # creating a dict for input assignment

    valid = False
    while not valid:
        print(f"{player}'s turn")
        user_input = input("Enter the coordinates: ")
        if user_input.replace(' ', '').isalpha():
            print("You should enter numbers!")
        elif user_input.replace(' ', '').isdigit():
            out = [int(nums) for nums in user_input.split() if int(nums) > total_cells]
            if out:
                print(f"Coordinates should be from 1 to {total_cells}!")
            elif user_input in initial_dict.keys():
                if initial_dict[user_input] != '-':
                    print("This cell is occupied! Choose another one")
                elif initial_dict[user_input] == '-':
                    valid = True

                    # vertical_check = [['0', '3', '6'], ['1', '4', '7'], ['2', '5', '8']]
                    vertical_check = which_vertical(''.join(list(initial_dict.values())), rows)

                    # ['0', '3', '6'], ['1', '4', '7'], ['2', '5', '8']
                    for lst in range(len(vertical_check)):
                        for i in range(1, rows + 1):
                            # provides an answer to which list has user_input
                            # if all the cells below are empty, first fills the empty cells
                            if user_input in vertical_check[lst]:
                                # check if initial_dict[0][-1]
                                if initial_dict[vertical_check[lst][-1 * i]] == '-':
                                    initial_dict[vertical_check[lst][-1 * i]] = player
                                    break

        print_tic(total_cells, initial_dict)
    return initial_dict


def flip_player(current_player):
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return current_player


# main
def four_in_a_row():
    increase_in_rows = 4
    rows = 3 + increase_in_rows
    win = 4

    # left - right
    slice = 3 + increase_in_rows
    diag_step_lr = 4 + increase_in_rows
    step1 = 0
    step2 = step1 + rows

    # right - left
    diag_step_rl = 2 + increase_in_rows
    step3 = 2 + increase_in_rows
    step4 = step3 + rows

    total_cells = (rows ** 2)

    initial_dict = empty_cells(total_cells, rows)
    current_player = 'X'

    for i in range(total_cells):
        states = tic_tac_cell_state(total_cells, current_player, initial_dict, rows)

        if horizon(states, rows, current_player, win) \
                or verticals(states, rows, current_player, win) \
                or diags(states, diag_step_lr, diag_step_rl, rows, slice, step1, step2, step3, step4, current_player,
                         win):
            break
        # print(initial_dict)
        current_player = flip_player(current_player)

    else:
        print("Draw")


four_in_a_row()
