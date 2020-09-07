def cominors_all_elements(matrix):
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
    matrix_all = cominors_all_elements(matrix)
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

    matrix_nested = []
    for i in range(0, len(matrix_of_cofactors()), len(matrix)):
        matrix_nested.append(matrix_of_cofactors()[i:i + len(matrix)])
    return matrix_nested



def cominors(matrix):
    one_matrix = []
    for i, j in enumerate(matrix):
        new_matrix = matrix[1:]  # deleting the row in the new matrix 2x3
        for index, elements in enumerate(new_matrix):  # index = 0, 1
            # new_matrix[0] = new_matrix[0][0:0] + new_matrix[0][1:]
            # new_matrix[1] = new_matrix[0][0:0] + new_matrix[0][1:]
            # element 2
            # new_matrix[0] = new_matrix[0][0:1] + new_matrix[0][2:]
            # new_matrix[1] = new_matrix[0][0:1] + new_matrix[0][2:]
            new_matrix[index] = new_matrix[index][0:i] + new_matrix[index][i + 1:]
        one_matrix.append(new_matrix)
    return one_matrix


def determinant(matrix, total=0):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    # base output when it is 2x2
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    # actual breaking down the matrix
    new_matrix = cominors(matrix)
    for i, j in enumerate(matrix):  # if matrix == 3x3, i = 0, 1, 2
        # changing the signs
        signs = (-1) ** (i % 2)

        # sub_det returns the answer of the 2x2 matrix if we have the 2x2
        # else breaks the matrix down
        sub_det = determinant(new_matrix[i])
        total += signs * matrix[0][i] * sub_det
    return total


matrix = [[4, 2, 3, 9], [-2, 4, 7, -7], [2, 3, 11, 1], [1, 1, 2, 0]]  # answer = -224
# print(cominors(matrix))
# print(determinant(matrix))
# print(cominors_all_elements(matrix))
# print(determinant_minors(matrix))
print(matrix_of_cofactors())
print(adjugate_matrix())