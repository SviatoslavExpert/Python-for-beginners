def find_max(user_list):
    max_number = user_list[0]
    for element in user_list:
        if element > max_number:
            max_number = element
    return max_number


my_list = [0,6,2,10,-2,4]

number = find_max(my_list)
print("Max = ",number)