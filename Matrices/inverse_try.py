def cominors(new_matrix, copy_matrix):
    for i in range(len(matrix)):
        new_matrix.append([item[:i] + item[i + 1:] for item in copy_matrix])
    return new_matrix


def cominors_all(matrix):
    matrix_all = []
    for j in range(len(matrix)):
        copy_matrix = matrix[:]
        row_pop = j
        matrix_row_removal = copy_matrix.pop(row_pop)
        for i in range(len(matrix)):
            matrix_all.append([item[:i] + item[i + 1:] for item in copy_matrix])
    return matrix_all


def determinant_minors(matrix):
    det_all = []
    matrix_all = cominors_all(matrix)
    for element in matrix_all:
        det_all.append(determinant(element))
    return det_all


def matrix_of_cofactors():
    mat_of_cofactors = []
    for elements in range(len(determinant_minors(matrix))):
        if elements % 2 == 0:
            mat_of_cofactors.append(determinant_minors(matrix)[elements])
        else:
            mat_of_cofactors.append(determinant_minors(matrix)[elements] * -1)
    return mat_of_cofactors



def determinant(matrix):
    det = 0
    row_pop = 0
    if len(matrix) == 1:
        det = matrix[0][0]
    elif len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        new_matrix = []
        copy_matrix = matrix[:]
        matrix_row_removal = copy_matrix.pop(row_pop)
        cominors(new_matrix, copy_matrix)
        print(cominors(new_matrix, copy_matrix))

        # for i in range(len(matrix)):
        #     # print(matrix[i])
        #     signs = (-1) ** i
        #     # print(signs)
        #     elements = matrix[row_pop][i]
        #     # print(elements)
        #     # print(new_matrix[i])
        #     # print()
        #     det += signs * elements * determinant(new_matrix[i])
    return det


matrix = [[4, 2, 3, 9], [-2, 4, 7, -7], [2, 3, 11, 1], [1, 1, 2, 0]]  # answer = -224
# matrix = [[4,7,-7], [3,11,1], [1,2,0]]

rows, columns = len(matrix), len(matrix[0])
print(determinant(matrix))
# print(determinant_minors(matrix))
# print(matrix_of_cofactors())

