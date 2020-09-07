def create_matrix_blueprint(label=""):
    print(f"Enter size of {label}matrix: > ", end='')
    rows, columns = map(int, input().split('\n')[0].split())
    print(f"Enter {label} matrix:")
    mat = []
    # counter to create an empty matrix
    i = 0
    while rows != 0:
        numbers = input().split()
        if len(numbers) != columns:
            pass
        else:
            mat.append([])
            for elements in numbers:
                if elements.isdigit():
                    mat[i].append(int(elements))
                elif str(-1 * float(elements)).isdigit():
                    mat[i].append(int(elements))
                else:
                    mat[i].append(float(elements))

            i += 1
            rows -= 1

    return mat


def add(matrix1, matrix2, rows1, rows2, columns1, columns2):
    add_res = []
    # self = matrix1, other = matrix 2
    if rows1 != rows2 and columns1 != columns2:
        return None
    else:
        for i in range(len(matrix1)):
            for elements in range(len(matrix1[i])):
                add_res.append(matrix1[i][elements] + matrix2[i][elements])
        return add_res


def mul_constant(matrix1):
    mult_constant = []
    number = input("Enter constant: > ")
    if number.isdigit():
        mul_number = int(number)
    else:
        mul_number = float(number)
    for i, j in enumerate(matrix1):
        for elements in j:
            mult_constant.append(mul_number * elements)
    return mult_constant


def mul_mat(matrix1, matrix2, rows1, rows2, columns1, columns2):
    mul_matrices = []
    # self = matrix1, other = matrix 2
    if columns1 == rows2:

        mul = []
        mul1 = []

        """
        Test matrix:
        matrix1 = [[1, 4, 5, 6, 6], [7, 8, 9, 0, 0], [4, 1, 2, 2, 2]]
        matrix2 = [[4, 5], [6, 1], [6, 0], [0, 9], [7, 7]]
        """

        for i in range(len(matrix1)):  # 3
            for k in range(len(matrix2[0])):  # 2
                for j in range(len(matrix2)):  # 5
                    mul.append([matrix1[i][j], matrix2[j][k]])
                    mul1.append(matrix1[i][j] * matrix2[j][k])
        # print(mul)
        # print(mul1)

        # add the results
        for i in range(0, len(mul1), len(matrix1[0])):
            mul_matrices.append(sum(mul1[i:i + len(matrix1[0])]))
        return mul_matrices
    else:
        return None


def transpose_choice():
    choices = input(
        "1. Main diagonal\n"
        "2. Side diagonal\n"
        "3. Vertical line\n"
        "4. Horizontal line\n"
        "Your choice: > \n"
    )

    if choices == '1':
        matrix = create_matrix_blueprint()
        output = main_diagonal(matrix)
        print_output(output, len(matrix))

    elif choices == '2':
        matrix = create_matrix_blueprint()
        output = side_diagonal(matrix)
        print_output(output, len(matrix))

    elif choices == '3':
        matrix = create_matrix_blueprint()
        output = vertical_line(matrix)
        print_output(output, len(matrix))

    elif choices == '4':
        matrix = create_matrix_blueprint()
        output = horizontal_line(matrix)
        print_output(output, len(matrix))


def main_diagonal(matrix):
    # transposing matrix
    # method 1
    # new_matrix = []
    # for i in range(len(matrix[0])):
    #     new_matrix.append([])
    # for i, j in enumerate(matrix):
    #     for k, l in enumerate(j):
    #         new_matrix[k].append(l)
    #
    # new_mat = []
    # for i, j in enumerate(new_matrix):
    #     for elements in j:
    #         new_mat.append(elements)
    # return new_mat

    # method 2
    new_matrix = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            new_matrix.append(matrix[j][i])
    return new_matrix


def side_diagonal(matrix):
    # method 1
    output = main_diagonal(matrix)
    output.reverse()
    return output

    # # method 2
    # new_matrix = []
    # for i in range(len(matrix) - 1, -1, -1):
    #     for j in range(len(matrix[i]) - 1, -1, -1):
    #         new_matrix.append(matrix[j][i])
    # return new_matrix


def vertical_line(matrix):
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    new_matrix = []
    for i, j in enumerate(matrix):
        j.reverse()
        for elements in j:
            new_matrix.append(elements)
    return new_matrix


def horizontal_line(matrix):
    matrix.reverse()
    new_mat = []
    for i, j in enumerate(matrix):
        for elements in j:
            new_mat.append(elements)
    return new_mat


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


def change_signs(matrix):
    """
    merge main matrix with the result to get all possible numbers to change signs.
    sort them according to the size(len) of the matrix
    get the first matrix in the list of lists as long as the elements are more than 2

    """

    new_list = sort_matrices(matrix)

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


def multiplication_cofactors(matrix):
    multiplication_cofactor = []
    for i in range(len(sort_matrices(matrix))):
        # print(sort_matrices()[i])
        # print(len(sort_matrices()))
        if len(sort_matrices(matrix)[i]) == 2:
            mul1 = sort_matrices(matrix)[i][0][0] * sort_matrices(matrix)[i][1][1]
            mul2 = sort_matrices(matrix)[i][0][1] * sort_matrices(matrix)[i][1][0]
            final_output = mul1 - mul2
            multiplication_cofactor.append(change_signs(matrix)[i] * final_output)
    return multiplication_cofactor


def add_mul_add(matrix, multiplication_cofactor, step):
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
                output.append(change_signs(matrix)[i] * add[add_step])
                add_step += 1

    return output


def recurse_cofactor(matrix, step):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        mul1 = matrix[0][0] * matrix[1][1]
        mul2 = matrix[0][1] * matrix[1][0]
        return mul1 - mul2

    else:
        output = add_mul_add(matrix, multiplication_cofactors(matrix), step)
        if len(output) == 1:
            return sum(output)
        else:
            while step < len(matrix):
                step += 1
                output = output + add_mul_add(matrix, output, step)
            else:
                if len(output) == len(matrix[0]):
                    return sum(output)
            return sum(output[-1 * (len(matrix) + 1):-1])


# matrix = [[4, 2], [-2, 4]] # answer = 20
# # matrix = [[4, 2, 3, 9], [-2, 4, 7, -7], [2, 3, 11, 1], [1, 1, 2, 0]] # answer = -224
# # matrix = [[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]] # answer = 191
# # matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]] # answer = -306
# # print(get_matrices(matrix))
# # print(sort_matrices(matrix))
# # print(change_signs())
# # print(multiplication_cofactors())
#
# # # the first draft after all the matrices and the numbers are out
# # for i in range(len(sort_matrices(matrix))):
# #     print(change_signs()[i], sort_matrices(matrix)[i])
#
# print(recurse_cofactor(3))



def print_output(output, columns2):
    if output is None:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        for all_elements in range(0, len(output), columns2):
            print(*output[all_elements:all_elements + columns2])

    print()


def main():
    matrix_calc = True
    while matrix_calc:
        user_input = input("1. Add matrices\n"
                           "2. Multiply matrix by a constant\n"
                           "3. Multiply matrices\n"
                           "4. Transpose matrix\n"
                           "5. Calculate a determinant\n"
                           "0. Exit\n"
                           "Your choice: > ")
        if user_input == '1':

            matrix1 = create_matrix_blueprint(label="first ")
            matrix2 = create_matrix_blueprint(label="second ")

            output = add(
                matrix1, matrix2,
                rows1=len(matrix1),
                rows2=len(matrix2),
                columns1=len(matrix1[0]),
                columns2=len(matrix2[0])
            )
            print_output(output, columns2=len(matrix2[0]))

        if user_input == '2':
            matrix = create_matrix_blueprint()
            output = mul_constant(matrix)
            print_output(output, len(matrix[0]))

        if user_input == '3':
            matrix1 = create_matrix_blueprint(label="first ")
            matrix2 = create_matrix_blueprint(label="second ")
            output = mul_mat(
                matrix1, matrix2,
                rows1=len(matrix1),
                rows2=len(matrix2),
                columns1=len(matrix1[0]),
                columns2=len(matrix2[0])
            )
            print_output(output, columns2=len(matrix2[0]))

        if user_input == '4':
            transpose_choice()

        if user_input == '5':
            matrix = create_matrix_blueprint()
            print("The result is:")
            print(recurse_cofactor(matrix, 3))

        if user_input == '0':
            matrix_calc = False


main()
