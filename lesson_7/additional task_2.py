word_1 = input("Input first word:  ")
word_2 = input("Input second word:  ")
matrix = []
for i in range(len(word_1) + 1):
    row = []
    for j in range(len(word_2) + 1):
        row.append(0)
    matrix.append(row)

for i in range(len(word_2)+1):
    matrix[0][i] = i
for i in range(len(word_1)+1):
    matrix[i][0] = i

for i in range(1, len(word_1) + 1):
    for j in range(1, len(word_2) + 1):
        if word_1[i - 1] == word_2[j - 1]:
            change = 0
        else:
            change = 1
        matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + change )

print("Levenshtein distance between ", word_1, " and ", word_2, " = ", matrix[len(word_1)][len(word_2)])
