def find_element(user_list, number):
    for i in range(len(user_list)):
        if user_list[i] == number:
            return i
    return -1

user_list = [0,3,2,7,1]

print(find_element(user_list, 2))
print(find_element(user_list, 10))