n = int(input("input n: "))
if n > 4 and n < 16:
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print(n,"!= ",fact)
else:
    print("You input wrong number")
