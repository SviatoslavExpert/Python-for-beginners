i = 2
while i <= 100:
    prime = True
    j = 2
    while j < i:
        if i % j == 0:
            prime = False
            break
        j = j + 1
    if prime:
        print(i)
    i = i + 1