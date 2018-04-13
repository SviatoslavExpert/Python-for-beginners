list_1 = []
list_2 = []
for i in range(100):
    if i % 3 == 0:
        list_1.append(i)
    if i % 5 == 0:
        list_2.append(i)
result_set = set(list_1).intersection(set(list_2))
print(result_set)