number = int(input("Input  number:  "))

part_1 = number // 100000
part_2 = number % 100000 // 10000
part_3 = number % 10000 // 1000
part_4 = number %1000 // 100
part_5 = number %100 // 10
part_6 = number %10 // 1


if  part_1 == part_6  and  part_2 == part_5 and part_3 == part_4 :
    print(number, " is palindrome")
else:
    print(number, " not palindrome")
