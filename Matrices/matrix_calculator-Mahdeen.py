# Mahdeen sky
# stage 1/6: Addition
class MatrixCalculator:

    def __init__(self):
        self.matrixes = []
        self.res_matrix = []
        self.dimensions = []

    def set_matrix_dimension(self):
        self.dimensions.append([int(dim) for dim in input().split()])

    def get_matrix_dimension(self, number):
        return self.dimensions[number]

    def input_matrix(self, number):
        temp_matrix = []
        for _ in range(self.get_matrix_dimension(number)[0]):
            temp_matrix.append([int(element) for element in input().split()])
        self.matrixes.append(temp_matrix)

    def check_matrix_dimension(self, operation):
        if operation == '+' or operation == '-':
            matrix1 = self.get_matrix_dimension(0)
            matrix2 = self.get_matrix_dimension(1)
            if matrix1 != matrix2:
                return False
        return True

    def format_output(self):
        for row in self.res_matrix:
            for column in row:
                print(column, end=' ')
            print()

    def error_handling(self, operation):
        if operation == '+':
            print("ERROR")

    def addition(self):
        self.set_matrix_dimension()
        self.input_matrix(0)
        self.set_matrix_dimension()
        self.input_matrix(1)

        if self.check_matrix_dimension('+'):
            for row in range(self.get_matrix_dimension(0)[0]):
                row_temp = []
                for column in range(self.get_matrix_dimension(0)[1]):
                    row_temp.append(self.matrixes[0][row][column] + self.matrixes[1][row][column])
                self.res_matrix.append(row_temp)

            self.format_output()

        else:
            self.error_handling('+')

    def main(self):
        self.addition()


MatrixCalculator().main()