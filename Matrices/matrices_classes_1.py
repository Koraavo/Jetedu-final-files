class Matrix:
    def __init__(self):
        # get rows and columns



        # create matrix for objects
        self.matrix = self.create_matrix()

        # results
        self.add_res = []
        self.mul_constant = []
        self.mul_matrices = []


    def create_matrix(self):
        mat = []
        for i in range(self.rows):
            numbers = input().split()
            # are elements in the matrix == columns?
            # enter data again in case false
            if len(numbers) != self.columns:
                pass
            else:
                mat.append(numbers)

        # str to int
        new_list = [[float(elements) for elements in j] for i, j in enumerate(mat)]
        return new_list

    def add(self, other):
        # self = matrix1, other = matrix 2
        if self.rows != other.rows and self.columns != other.columns:
            return None
        else:
            for i in range(len(self.matrix)):
                for elements in range(len(self.matrix[i])):
                    self.add_res.append(int(self.matrix[i][elements]) + int(other.matrix[i][elements]))
            return self.add_res

    def multiply(self, mul_number):
        for i, j in enumerate(self.matrix):
            for elements in j:
                self.mul_constant.append(mul_number * elements)
        return self.mul_constant

    def mul_mat(self, other):
        # self = matrix1, other = matrix 2
        if self.columns == other.rows:

            # self.rows1 = len(self.matrix)
            # self.rows2 = len(other.matrix)
            # self.columns1 = [len(i) for i in self.matrix][0]
            # self.columns2 = [len(i) for i in other.matrix][0]
            # final_matrix_size = [self.rows1, self.columns2]
            # print(final_matrix_size)

            new_matrix = []
            for i in range(len(other.matrix[0])):
                new_matrix.append([])
            for i, j in enumerate(other.matrix):
                for k, l in enumerate(j):
                    new_matrix[k].append(l)
            # print(new_matrix)

            for i, elements in enumerate(new_matrix):
                for j, elements1 in enumerate(self.matrix):
                    mat_add = sum([(elements1[i] * elements[i]) for i in range(len(elements))])
                    self.mul_matrices.append(mat_add)
            return self.mul_matrices
        else:
            return None

    def print_output(self, output):
        if output is None:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            for all_elements in range(0, len(output), self.columns):
                print(''.join(str(output[all_elements:all_elements + self.columns])).strip('[]').replace(',', ' '))
        print()


def rows_columns():
    rows, columns = map(int, input().split('\n')[0].split())
    return rows, columns


def main():
    matrix_calc = True
    while matrix_calc:
        user_input = input(
            "1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit\nYour choice: > ")
        if user_input == '1':
            print(f"Enter size of first matrix: > ", end='')
            rows_columns()
            matrix1 = Matrix()
            print(f"Enter size of second matrix: > ", end='')
            matrix2 = Matrix()
            output = matrix1.add(matrix2)
            matrix1.print_output(output)

        if user_input == '2':
            print(f"Enter size of matrix: > ", end='')
            matrix1 = Matrix()
            output = matrix1.multiply(float(input("Enter constant: > ")))
            matrix1.print_output(output)

        if user_input == '3':
            print(f"Enter size of first matrix: > ", end='')
            matrix1 = Matrix()
            print(f"Enter size of second matrix: > ", end='')
            matrix2 = Matrix()
            output = matrix1.mul_mat(matrix2)
            matrix1.print_output(output)

        if user_input == '0':
            matrix_calc = False


main()
