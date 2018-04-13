n = int(input("input clock size: "))
if n % 2 == 1:
    i = 0
    j = 0
    while i < n:
        while j < n:
            if j >= n//2 - abs(n//2 - i) and j <= n//2 + abs(n//2-i):
                print("*",end="")
            else:
                print(" ",end="")
            j = j + 1
        print()
        i = i + 1
        j = 0