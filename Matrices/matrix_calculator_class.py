class matrix:
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.elements = []

    def append_row(self, row):
        if len(row) == self.col_size:
            self.elements.append(row)
        else:
            print(f"No of elements must be {self.col_size}")

    def __add__(self, other):
        if self.row_size == other.row_size and self.col_size == other.col_size:
            new_matrix = matrix(self.row_size, self.col_size)
            for i in range(self.row_size):
                new_matrix.append_row([self.elements[i][j] + other.elements[i][j] for j in range(self.col_size)])
            return new_matrix
        else:
            return "The operation cannot be performed"

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_matrix = matrix(self.row_size, self.col_size)
            for row in self.elements:
                new_matrix.append_row([element * other for element in row])
            return new_matrix
        elif isinstance(other, matrix):
            if self.col_size == other.row_size:
                new_matrix = matrix(self.row_size, other.col_size)
                for i in range(self.row_size):
                    new_row = []
                    for j in range(other.col_size):
                        new_row.append(sum([self.elements[i][k] * other.elements[k][j] for k in range(self.col_size)]))
                    new_matrix.append_row(new_row)
                return new_matrix
            return "The operation cannot be performed"

    def transpose(self, mirror="main"):
        if mirror == "main":
            new_matrix = matrix(self.col_size, self.row_size)
            for i in range(self.col_size):
                new_matrix.append_row([self.elements[j][i] for j in range(self.row_size)])
            return new_matrix
        if mirror == "side":
            new_matrix = matrix(self.col_size, self.row_size)
            for i in range(self.col_size - 1, -1, -1):
                new_matrix.append_row([self.elements[j][i] for j in range(self.row_size - 1, -1, -1)])
            return new_matrix
        if mirror == "hor":
            new_matrix = matrix(self.row_size, self.col_size)
            new_matrix.elements = reversed(self.elements)
            return new_matrix
        if mirror == "ver":
            new_matrix = matrix(self.row_size, self.col_size)
            for row in self.elements:
                new_matrix.append_row(list(reversed(row)))
            return new_matrix

    def __str__(self):
        string_form = f""
        for row in self.elements:
            for element in row:
                string_form += str(element) + " "
            string_form += "\n"
        return string_form


def generate_matrix(label):
    print(f"Enter size of {label}matrix")
    row_size, col_size = [int(num) for num in input().split()]
    new_matrix = matrix(row_size, col_size)
    print(f"Enter {label}matrix")
    for _ in range(row_size):
        new_matrix.append_row([float(num) for num in input().split()])
    return new_matrix


def get_input(action):
    if action in (1, 3):
        return generate_matrix("first "), generate_matrix("second ")
    if action == 2:
        matrix1 = generate_matrix("")
        num = float(input("Enter constant: "))
        return matrix1, num
    if action == 4:
        choice = int(input("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n"
                           + "4. Horizontal line\nYour choice: "))
        if choice == 1:
            mirror = "main"
        elif choice == 2:
            mirror = "side"
        elif choice == 3:
            mirror = "ver"
        elif choice == 4:
            mirror = "hor"
        return generate_matrix(""), mirror


def run():
    while True:
        action = int(input("1. Add matrices\n2. Multiply matrix by a constant\n"
                           + "3. Multiply matrices\n4. Tranpose matrix\n0. Exit\nYour choice: "))
        if action == 1:
            matrix1, matrix2 = get_input(action)
            print("The result is:", matrix1 + matrix2, sep="\n")
        elif action == 2:
            matrix1, num = get_input(action)
            print("The result is:", matrix1 * num, sep="\n")
        elif action == 3:
            matrix1, matrix2 = get_input(action)
            print("The result is:", matrix1 * matrix2, sep="\n")
        elif action == 4:
            matrix1, mirror = get_input(action)
            print("The result is: ", matrix1.transpose(mirror), sep="\n")
        else:
            break


if __name__ == "__main__":
    run()