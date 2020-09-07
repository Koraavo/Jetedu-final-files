def createMatrix(rowCount, colCount, dataList):
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            # you need to increment through dataList here, like this:
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)
    # print(mat)
    return mat

# Driver code
lst = list(range(49)) # creates a list with elements 0 to 48
mat = createMatrix(7, 7, lst) # creates the matrix
Seclst = []
for offset in range(7):
    diag = [row[i+offset] for i,row in enumerate(mat) if 0 <= i+offset < len(row)]
    print(diag)
    Seclst.append(diag)
# for offset in range(7):
#     diag2 = [row[i + offset] for i, row in enumerate(mat) if 0 <= i + offset < len(row)]
#     print(diag2)

print(Seclst)