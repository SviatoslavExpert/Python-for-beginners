max_heigth = int(input("input max heigth: "))
i = 0
j = 0
while i < 2 * max_heigth - 1:
    if j >= max_heigth - abs(max_heigth - i):
        i = i + 1
        print()
        j = 0
    print("*",end = "")
    j = j + 1
print()