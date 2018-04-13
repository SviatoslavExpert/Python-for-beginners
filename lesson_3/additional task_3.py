number = int(input("Input ticket number:  "))

part_1 = number // 1000
part_2 = number % 1000 // 100
part_3 = number % 100 // 10
part_4 = number %10

if  part_1 + part_2 == part_3 + part_4:
    print("You have a lucky ticket")
else:
    print("You have an ordinary ticket")
