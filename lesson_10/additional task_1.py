def input_sequince():
    seq = input(" Input sequince:  ")
    number_list = []
    seq_list = seq.split(",")
    for element in seq_list:
        number_list.append(int(element))
    return number_list

def is_same(number_list):
    for i in range(len(number_list) - 1):
        if number_list[i+1] != number_list[i]:
            return False
    return True

def is_ariphmetic(number_list):
    temp_list = []
    for i in range(len(number_list) - 1):
        temp_list.append(number_list[i+1] - number_list[i])
    if is_same(temp_list) == True:
        return number_list[len(number_list) - 1] + temp_list[0]
    else:
        return None

def is_geometric(number_list):
    temp_list = []
    for i in range(len(number_list) - 1):
        if number_list[i] == 0:
            return None
        if number_list[i+1] % number_list[i] != 0:
            return None
        temp_list.append(number_list[i+1]//number_list[i])
    if is_same(temp_list) == True:
        return number_list[len(number_list) - 1] * temp_list[0]
    else:
        return None

def shipht(number_list):
    temp_list = []
    for i in range(len(number_list) - 1):
        temp_list.append(number_list[i+1]-number_list[i])
    return temp_list


def is_pow(number_list):
    n = 1
    temp_list = shipht(number_list)
    while True:
        temp_list = shipht(temp_list)
        n += 1
        if len(temp_list) == 1:
            return None
        if is_same(temp_list):
            break
    last_number = round(number_list[len(number_list)-1]**(1/n))
    return (last_number + 1)**n


def solve_task():
    res = input_sequince()
    if is_ariphmetic(res)  is not None:
        print(res,"next is -> ",is_ariphmetic(res))
    elif is_geometric(res) is not None:
        print(res,"next is -> ",is_geometric(res))
    elif is_pow(res) is not None:
        print(res,"next is -> ",is_pow(res))
    else:
        print(res," next is -> Not correct sequince")

solve_task()
