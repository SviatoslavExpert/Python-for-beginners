import random

matrix = []
for i in range(6):
    matrix.append(random.randint(0,9))
print(matrix)
print("Mirror matrix")
for i in range(len(matrix)//2):
    matrix[i],matrix[len(matrix)-i-1] = matrix[len(matrix)-i-1], matrix[i]
print(matrix)

