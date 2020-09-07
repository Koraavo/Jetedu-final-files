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

"""


def diagslr(states):
    diag_step = 8
    diag1_step = 6
    player = 'X'
    win = 4
    rows = 7
    slice = 7
    slice1 = 7
    step1 = 0
    step2 = step1 + 7
    step3 = 6
    step4 = step3 + 7
    while step1 < rows:
        diag1 = ([i for i in range(step1, len(states), diag_step)][0:slice])
        step1 += 1
        slice -= 1
        diag2 = [i for i in range(step2, len(states), diag_step)]
        step2 += rows

        diag3 = ([i for i in range(step3, len(states), diag1_step)][0:slice1])
        step3 -= 1
        slice1 -= 1
        diag4 = [i for i in range(step4, len(states), diag1_step)]
        step4 += rows
        yield diag1
        yield diag2
        yield diag3
        yield diag4

states=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48']
final_list = diagslr(states)
# removes empty lists, empty tuples, 0s etc from the final_list
list2 = [x for x in final_list if x]
print(list(list2))


# output = [[0, 8, 16, 24, 32, 40, 48], [1, 9, 17, 25, 33, 41], [2, 10, 18, 26, 34], [3, 11, 19, 27], [4, 12, 20], [5, 13], [6]]

