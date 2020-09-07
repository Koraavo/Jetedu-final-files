def determinant_matrix(matrix_a):
    dim = len(matrix_a)
    det = 0

    # base cases
    if dim == 1:
        det = matrix_a[0][0]
    if dim == 2:
        det = matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0]
    # general case
    if dim > 2:
        for j in range(dim):
            matrix_minor = []
            cofactor = (-1) ** j
            a_elem = matrix_a[j][0]
            for i in range(dim):
                if j != i:
                    matrix_minor.insert(i, matrix_a[i][1:])
                print(determinant_matrix(matrix_minor))
            det += cofactor * a_elem * determinant_matrix(matrix_minor)
        # return print_result(det)
    return det


# matrix = [[4, 2], [-2, 4]] # answer = 20
matrix = [[4, 2, 3, 9], [-2, 4, 7, -7], [2, 3, 11, 1], [1, 1, 2, 0]]  # answer = -224
# # matrix = [[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]] # answer = 191
# # matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]] # answer = -306

print(determinant_matrix(matrix))
