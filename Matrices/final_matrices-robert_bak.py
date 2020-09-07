def create_matrix(word):
    n, m = map(int, input(f'Enter size of {word} matrix: ').split())
    print(f'Enter {word} matrix:')
    return [[float(x) for x in input().split()] for i in range(n)]


def formatted(matrix):
    s = ''
    for row in matrix:
        s = s + '\n' + ' '.join(map(str, row))
    return s


def add(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        return 'The operation cannot be performed.'

    return [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]


def add_matrices():
    matrix_1 = create_matrix('first')
    matrix_2 = create_matrix('second')
    print(f'The result is:{formatted(add(matrix_1, matrix_2))}')


def multiply_by_const(matrix, c):
    return [[matrix[i][j] * c for j in range(len(matrix[0]))] for i in range(len(matrix))]


def multiply_matrix_by_const():
    matrix = create_matrix('')
    c = float(input('Enter constant: '))
    print(f'The result is:{formatted(multiply_by_const(matrix, c))}')


def multiply(matrix_1, matrix_2):
    if len(matrix_1[0]) != len(matrix_2):
        return 'The operation cannot be performed.'

    matrix = [[0 for j in range(len(matrix_2[0]))] for i in range(len(matrix_1))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_1[0])):
                matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return matrix


def multiply_matrices():
    matrix_1 = create_matrix('first')
    matrix_2 = create_matrix('second')
    print(f'The result is:{formatted(multiply(matrix_1, matrix_2))}')


def transpose(matrix, a):
    if a == '1':
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    elif a == '2':
        return [[matrix[i][j] for i in range(len(matrix) - 1, -1, -1)] for j in range(len(matrix[0]) - 1, -1, -1)]
    elif a == '3':
        return [row[::-1] for row in matrix]
    elif a == '4':
        matrix.reverse()
        return matrix


def transpose_matrix():
    a = input(transposition_menu)
    matrix = create_matrix('')
    print(f'The result is:{formatted(transpose(matrix, a))}')


def minor(matrix, n, m):
    return [[matrix[i][j] for j in range(len(matrix[0])) if j != m] for i in range(len(matrix)) if i != n]


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    res = 0
    for j in range(len(matrix[0])):
        res += matrix[0][j] * (-1) ** j * determinant(minor(matrix, 0, j))

    return res


def determinant_of_matrix():
    matrix = create_matrix('')

    if len(matrix) != len(matrix[0]):
        print('The operation cannot be performed.')

    else:
        print(f'The result is:\n{determinant(matrix)}')


def inverse(matrix):
    adj = [[(-1) ** (i + j) * determinant(minor(matrix, i, j)) for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return multiply_by_const(transpose(adj, '1'), 1 / determinant(matrix))


def inverse_of_matrix():
    matrix = create_matrix('')

    if determinant(matrix) == 0:
        print('The operation cannot be performed.')

    else:
        print(f'The result is:{formatted(inverse(matrix))}')


transposition_menu = '''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: '''

menu = '''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: '''

while True:
    action = input(menu)

    if action == '0':
        break
    elif action == '1':
        add_matrices()
    elif action == '2':
        multiply_matrix_by_const()
    elif action == '3':
        multiply_matrices()
    elif action == '4':
        transpose_matrix()
    elif action == '5':
        determinant_of_matrix()
    elif action == '6':
        inverse_of_matrix()