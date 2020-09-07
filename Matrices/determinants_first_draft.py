def get_matrices(matrix):
    """
    test:               coordinates
    01 02 03 04         11 12 13 14
    05 06 07 08         21 22 23 23
    09 10 11 12         31 32 33 34
    13 14 14 16         41 42 43 44

    to get all the possible matrices:
    x = 1
    row = 1
    column = iterate
    if row = 1 and x = column: do something
    else: do nothing.
    loop again
    x = 2
    row = 1
    column = iterate till 2
    if row = 1 and x = 2 and column = 1: do nothing
    if row = 1 and x = 2 and column = 2: do something
    This returns a 3x3 matrix
    recurse through the 3x3 to get the 2x2 matrix
    check if matrix is 2x2: break
    """
    matrix1 = []
    for x in range(len(matrix)):
        matrix1.append([])
        for i in range(len(matrix)):
            matrix1[x].append([])
            for j in range(len(matrix[i])):
                if i + 1 != 1 and j + 1 != x + 1:
                    matrix1[x][i].append(matrix[i][j])

    # getting rid of empty lists
    output = [[elements[i] for i in range(len(elements)) if elements[i]] for elements in matrix1]

    # recurse
    for i in range(len(output)):
        if len(output[0]) != 2:
            output = output + get_matrices(output[i])
    return output


def sort_matrices(matrix):
    total_matrices = [matrix] + get_matrices(matrix)
    new_list = sorted(total_matrices, reverse=True, key=len)
    return new_list


def change_signs():
    """
    merge main matrix with the result to get all possible numbers to change signs.
    sort them according to the size(len) of the matrix
    get the first matrix in the list of lists as long as the elements are more than 2

    """

    new_list = sort_matrices(matrix)
    if len(new_list) == 2:
        return new_list
    else:
        matrix_numbers = []
        for i, j in enumerate(new_list):
            matrix_numbers.append(j[0])

        matrix_sign = [0]
        for i, j in enumerate(matrix_numbers):
            for k, l in enumerate(j):
                if k % 2 == 0:
                    matrix_sign.append(l)
                else:
                    matrix_sign.append(-1 * l)
        return matrix_sign


def multiplication_cofactors():
    multiplication_cofactor = []
    for i in range(len(sort_matrices(matrix))):
        # print(sort_matrices()[i])
        # print(len(sort_matrices()))
        if len(sort_matrices(matrix)[i]) == 2:
            mul1 = sort_matrices(matrix)[i][0][0] * sort_matrices(matrix)[i][1][1]
            mul2 = sort_matrices(matrix)[i][0][1] * sort_matrices(matrix)[i][1][0]
            final_output = mul1 - mul2
            multiplication_cofactor.append(change_signs()[i] * final_output)
    return multiplication_cofactor


def add_mul_add(multiplication_cofactor, step):
    add = [sum(multiplication_cofactor[i:i + step]) for i in range(0, len(multiplication_cofactor), step)]
    output = []
    add_step = 0
    for i in range(len(sort_matrices(matrix))):
        if len(add) == 1:
            output = add
        else:
            # check if first element in sort_matrices == step (starts with 3)
            if len(sort_matrices(matrix)[i]) == step:
                # add indices start with 0
                output.append(change_signs()[i] * add[add_step])
                add_step += 1

    return output


def recurse_cofactor(step):
    if len(matrix) == 2:
        mul1 = matrix[0][0] * matrix[1][1]
        mul2 = matrix[0][1] * matrix[1][0]
        return mul1 - mul2

    else:
        output = add_mul_add(multiplication_cofactors(), step)
        if len(output) == 1:
            return sum(output)
        else:
            while step < len(matrix):
                step += 1
                output = output + add_mul_add(output, step)
            else:
                if len(output) == len(matrix[0]):
                    return sum(output)
            return sum(output[-1 * (len(matrix) + 1):-1])


# matrix = [[4, 2], [-2, 4]] # answer = 20
# matrix = [[4, 2, 3, 9], [-2, 4, 7, -7], [2, 3, 11, 1], [1, 1, 2, 0]] # answer = -224
matrix = [[4, 1, 3, 8], [2, 6, 5, 9], [7, 3, 3, 0], [2, 7, 9, 1]]
# matrix = [[6,5,9], [3,3,0], [7,9,1]]
# matrix = [[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]] # answer = 191
# matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]] # answer = -306
# print(get_matrices(matrix))
print(sort_matrices(matrix))
# print(change_signs())
# print(multiplication_cofactors())

# # the first draft after all the matrices and the numbers are out
# for i in range(len(sort_matrices(matrix))):
#     print(change_signs()[i], sort_matrices(matrix)[i])

print(recurse_cofactor(3))
