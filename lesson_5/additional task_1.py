import random

matrix = []
for i in range(6):
    row = []
    for j in range(6):
        row.append(random.randint(0,9))
    matrix.append(row)

for row in matrix:
    print(row)

for rot in range(3):
    for i in range(len(matrix) // 2):
        for j in range(i,len(matrix)-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[len(matrix)-1-j][i]
            matrix[len(matrix)-1-j][i] = matrix[len(matrix)-1-i][len(matrix)-1-j]
            matrix[len(matrix)-1-i][len(matrix)-1-j] = matrix[j][len(matrix)-1-i]
            matrix[j][len(matrix)-1-i] = temp
    print("Rotate ",90*(rot+1))
    for row in matrix:
        print(row)