"""
-----------------
| - - - - - - - |	00 01 02 03 04 05 06
| - - - - - - - |	07 08 09 10 11 12 13
| - - - - - - - |	14 15 16 17 18 19 20
| - - - - - - - |	21 22 23 24 25 26 27
| - - - - - - - |	28 29 30 31 32 33 34
| - - - - - - - |	35 36 37 38 39 40 41
| - - - - - - - |	42 43 44 45 46 47 48
-----------------

00 01 02 03 04
05 06 07 08 09
08 09 10 11
12 13 14 15

"""
"""
initial_dict = {}
diag_step_lr = 8
diag1_step_rl = diag_step_lr
player = 'X'
win = 4
rows = 7
slice = 7
step1 = 0
step2 = step1 + rows
step3 = 6
step4 = step3 + rows
key1 = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48']
value = ['-'] * 49
for index in range(len(key1)):
    initial_dict[key1[index]] = value[index]
print(initial_dict)

def diags(states, diag_step_lr, diag_step_rl, rows, slice, step1, step2, step3, step4, player):
    sec_list = []
    while step1 < rows:
        # range(0, 49, 8)[0:7]
        # left to right (+)
        # slice -= 1 ergo [0:6], [0:5] and so on
        diag1 = ([str(i).zfill(2) for i in range(step1, 49, diag_step_lr)][0:slice])
        # range(7, 49, 8)
        diag2 = [str(i).zfill(2) for i in range(step2, 49, diag_step_lr)[0:slice]]

        # range(6, 49, 6)[0:7]
        # right to left (-)
        diag3 = ([str(i).zfill(2) for i in range(step3, 49, diag_step_rl)][0:slice])
        # range(13, 49, 6)[0:7]
        diag4 = [str(i).zfill(2) for i in range(step4, 49, diag_step_rl)[0:slice]]

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
    # for i, j in enumerate(sec_list):
    #     if len(j) >= 4:
    #         check_list = sec_list
    #         print(check_list)
    print(sec_list)
    return sec_list

diags(initial_dict.values(), diag_step_lr, diag1_step_rl, rows, slice, step1, step2, step3, step4, player)"""
player = 'X'
initial_dict = {}
sec_list = [['00', '01', '02', '03', '04', '05', '06']]
list1 = ['00', '01', '02', '03', '04', '05', '06']
value = ['-'] * len(list1)
for index in range(len(list1)):
    initial_dict[list1[index]] = value[index]
initial_dict['03'] = 'X'
initial_dict['05'] = 'X'
states = ''.join(initial_dict.values())
for i, j in enumerate(sec_list):
    if str(states.index(player)).zfill(2) in j:
        num = [ele for ele in j if states[int(ele)] == player]
        print(num)