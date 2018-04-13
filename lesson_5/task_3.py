import random
my_list = []
for i in range(12):
    my_list.append(random.randint(7500,12000))
print(my_list)

summa = 0
for element in my_list:
    summa += element
summa = summa / len(my_list)
print("Average pay = ", summa)