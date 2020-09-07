def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        sum = 0
        for i in range(width):
         m = []
         for j in range(1, width):
          buff = []
          for k in range(width):
           if k != i:
            buff.append(matrix[j][k])
          m.append(buff)
         sign *= -1
         sum += mul * determinant(m, sign * matrix[0][i])
        return sum

# matrix = [[4, 2], [-2, 4]] # answer = 20
matrix = [[4, 2, 3, 9], [-2, 4, 7, -7], [2, 3, 11, 1], [1, 1, 2, 0]] # answer = -224
# # matrix = [[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]] # answer = 191
# # matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]] # answer = -306

print(determinant(matrix, 1))