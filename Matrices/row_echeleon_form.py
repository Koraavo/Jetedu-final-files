def create_identity_matrix(matrix):
    rows = len(matrix)
    matrix_i = []
    for i in range(rows):
        matrix_i.append([])
        for j in range(rows):
            if i == j:
                matrix_i[i].append(1)
            else:
                matrix_i[i].append(0)
    return matrix_i



matrix = [[4, 2, 3, 9], [-2, 4, 7, -7], [2, 3, 11, 1], [1, 1, 2, 0]]  # answer = -224
print(create_identity_matrix(matrix))