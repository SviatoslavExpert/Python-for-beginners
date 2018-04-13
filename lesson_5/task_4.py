matrix = []
number = 1
for i in range(4):
    cols = []
    for j in range(4):
        cols.append(number)
        number += 1
    matrix.append(cols)

for col in matrix:
    print(col)

summa = 0
for cols in matrix:
    for element in cols:
        summa += element

print("Summa = ",summa)