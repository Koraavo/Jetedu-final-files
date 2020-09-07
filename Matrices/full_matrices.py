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


def create_identity_matrix(label=""):
    print(f"Enter size of {label}matrix: > ", end='')
    rows, columns = map(int, input().split('\n')[0].split())
    matrix_i = []
    for i in range(rows):
        matrix_i.append([])
        for j in range(columns):
            if i == j:
                matrix_i[i].append(1)
            else:
                matrix_i[i].append(0)
    return matrix_i


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


def mul_constant(matrix1, number):
    mult_constant = []
    # number = input("Enter constant: > ")
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


def cominors(matrix):
    for i, j in enumerate(matrix):  # if matrix == 3x3, i = 0, 1, 2
        new_matrix = matrix[1:]  # deleting the row in the new matrix 2x3
        for index, elements in enumerate(new_matrix):  # index = 0, 1
            # new_matrix[0] = new_matrix[0][0:0] + new_matrix[0][1:]
            # new_matrix[1] = new_matrix[0][0:0] + new_matrix[0][1:]
            # element 2
            # new_matrix[0] = new_matrix[0][0:1] + new_matrix[0][2:]
            # new_matrix[1] = new_matrix[0][0:1] + new_matrix[0][2:]
            new_matrix[index] = new_matrix[index][0:i] + new_matrix[index][i + 1:]
        return new_matrix


def determinant(matrix, total=0):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    # base output when it is 2x2
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    # actual breaking down the matrix
    for i, j in enumerate(matrix):  # if matrix == 3x3, i = 0, 1, 2
        new_matrix = matrix[1:]  # deleting the row in the new matrix 2x3
        for index, elements in enumerate(new_matrix):  # index = 0, 1
            # new_matrix[0] = new_matrix[0][0:0] + new_matrix[0][1:]
            # new_matrix[1] = new_matrix[0][0:0] + new_matrix[0][1:]
            # element 2
            # new_matrix[0] = new_matrix[0][0:1] + new_matrix[0][2:]
            # new_matrix[1] = new_matrix[0][0:1] + new_matrix[0][2:]
            new_matrix[index] = new_matrix[index][0:i] + new_matrix[index][i + 1:]

        # print(new_matrix, matrix[0][i])

        # changing the signs
        signs = (-1) ** (i % 2)
        # print(signs)

        # sub_det returns the answer of the 2x2 matrix if we have the 2x2
        # else breaks the matrix down
        sub_det = determinant(new_matrix)
        total += signs * matrix[0][i] * sub_det
    return total


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

    matrix_nested = []
    for i in range(0, len(det_all), len(matrix)):
        matrix_nested.append(det_all[i:i + len(matrix)])
    return matrix_nested


def matrix_of_cofactors(matrix):
    minors = determinant_minors(matrix)
    matrix_cofactors = []
    for a, elements in enumerate(minors):
        for j, k in enumerate(elements):
            # changing the signs
            signs = (-1) ** ((a + j) % 2)
            matrix_cofactors.append(signs*minors[a][j])

    matrix_nested = []
    for i in range(0, len(matrix_cofactors), len(matrix)):
        matrix_nested.append(matrix_cofactors[i:i + len(matrix)])
    return matrix_nested


def adjugate_matrix(matrix):
    matrix_cofactors = matrix_of_cofactors(matrix)
    return main_diagonal(matrix_cofactors)


def multiply_by_determinant(matrix):
    determinant_matrix = determinant(matrix)
    matrix_nested = []
    for i in range(0, len(adjugate_matrix(matrix)), len(matrix)):
        matrix_nested.append(adjugate_matrix(matrix)[i:i + len(matrix)])

    return mul_constant(matrix_nested, str(1/determinant(matrix)))


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
                           "6. Calculate the inverse\n"
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
            output = mul_constant(matrix, input("Enter constant: > "))
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
            print(determinant(matrix))

        if user_input == '6':
            matrix = create_matrix_blueprint()
            output = multiply_by_determinant(matrix)
            print_output(output, columns2=len(matrix[0]))

        if user_input == '0':
            matrix_calc = False


main()
# matrix = [[2, -1, 0], [0,1,2], [1,1,0]]
# # matrix = [[4, 2, 3, 9], [-2, 4, 7, -7], [2, 3, 11, 1], [1, 1, 2, 0]]  # answer = -224
# # print(cominors(matrix))
# # print(determinant_minors(matrix))
# print(matrix_of_cofactors(matrix))
# print(adjugate_matrix(matrix))
# print(determinant(matrix))
# print(multiply_by_determinant(matrix))
# print(mul_constant(matrix))
