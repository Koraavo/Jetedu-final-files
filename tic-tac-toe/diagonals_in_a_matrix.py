a = """
00 01 02 03 04 05 06
07 08 09 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31 32 33 34
35 36 37 38 39 40 41
42 43 44 45 46 47 48
"""
c = a.split()
print(c)
# states = """[
# '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
# '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
# '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
# '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
# '44', '45', '46', '47', '48'
# ]"""


# new_list = [[c[(i * 7) + j] for j in range(7)] for i in range(7)]
# print(new_list)

new_list = []
for i in range(7):
    new_list.append([])  # creates an empty list everytime
    for j in range(7):
        # states[0 * 7 + 0] from 0 to 6, 7-14
        new_list[i].append(c[(i * 7) + j])  # append to the empty list (i = 0, j = [0-6], i = 1, j = [0-6] and so on)
print(new_list)


def diagonal(item):
    global c, new_list
    diag = []
    # position = c.index('00') // 7, c.index('00') // 7
    # position = c.index('01') // 7, c.index('01') // 7

    position = (c.index(item) // 7, c.index(item) % 7)

    for j in range(7):
        try:
            # new_list is a list of lists for the elements in states
            # diag.append(new_list[0][0]), new_list[1][1]
            diag.append(new_list[j + position[0]][j + position[1]])
        except IndexError:
            pass

    return diag

# 00, 01, 02, 03, 04, 05, 06, 07, 14, 21, 28, 35, 42
final_list = [diagonal(i) for i in new_list[0]] + [diagonal(i[0]) for i in new_list[1:]]
print(final_list)
