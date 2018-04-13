year = int(input("Input year:  "))
if year > 0:
    day = 365
    if year % 4 == 0:
        day = 366
    if year % 100 ==0:
        day = 365
    if year % 400 ==0:
        day = 366
    print("Days number = ", day)
else:
    print("Sorry but you input negative year")
