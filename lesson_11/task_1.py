def get_summ(user_list):
    summa = 0
    for element in user_list:
        if element % 2 == 1:
            summa += element
    return summa

user_list = [2, 1, 4, 6, 3]
print(get_summ(user_list))