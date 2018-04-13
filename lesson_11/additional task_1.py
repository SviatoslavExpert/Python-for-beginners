def find_one_permutation(user_list,arrow):
    max_index = None
    arr = None
    max_element = None
    for i in range(len(user_list)):
        if arrow[i] == 0 and i > 0 and user_list[i-1] < user_list[i] and (max_element is None or user_list[i] > max_element):
            max_index = i
            arr = arrow[i]
            max_element = user_list[i]
        if arrow[i] == 1 and i < len(user_list)-1 and user_list[i] > user_list[i+1] and (max_element is None or user_list[i] > max_element):
            max_index = i
            arr = arrow[i]
            max_element = user_list[i]
    return (max_element,max_index,arr)

def one_permutation(user_list, arrow, one_perm):
    max_element = one_perm[0]
    max_index = one_perm[1]
    arr = one_perm[2]
    if arr == 0:
        user_list[max_index], user_list[max_index-1] = user_list[max_index-1], user_list[max_index]
        arrow[max_index],arrow[max_index-1] = arrow[max_index-1],arrow[max_index]
    if arr == 1:
        user_list[max_index], user_list[max_index + 1] = user_list[max_index + 1], user_list[max_index]
        arrow[max_index],arrow[max_index+1] = arrow[max_index+1],arrow[max_index]
    for i in range(len(user_list)):
        if user_list[i] > max_element:
            if arrow[i] == 0:
                arrow[i] = 1
            else:
                arrow[i] = 0
    return user_list, arrow

def get_permutations(user_list):
    arrow = []
    for i in range(len(user_list)):
        arrow.append(0)
    permutations = []
    permutations.append(user_list.copy())
    one_perm = find_one_permutation(user_list,arrow)
    while one_perm[0] is not None:
        user_list, arrow = one_permutation(user_list, arrow, one_perm)
        permutations.append(user_list.copy())
        one_perm = find_one_permutation(user_list,arrow)
    return permutations


user_list = [1, 2, 3, 4]

perm_list = get_permutations(user_list)
for element in perm_list:
    print(element)
