import random
my_list = []
for i in range(4):
    my_list.append(random.randint(0,10))
print(my_list)

my_new_list = []
my_new_list.extend(my_list)
for element in my_list:
    my_new_list.append(2 * element)
print(my_new_list)