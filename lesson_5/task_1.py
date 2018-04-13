my_list = [0,5,2,4,7,1,3,19]
count = 0
for element in my_list:
    if element % 2 == 1:
        count += 1
print(my_list)
print("You have ",count, "odd number")