height = int(input("input rectangle height: "))
width = int(input("Input rectangle width: "))
i = 1
j = 1
while i <= height:
    while j <= width:
        if i == 1 or i == height or j == 1 or j == width:
            print("*", end="")
        else:
            print(" ", end="")
        j = j + 1
    print()
    i = i + 1
    j = 1
