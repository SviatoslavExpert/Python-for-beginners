mount = [
    [7],
    [5, 8],
    [9, 8, 2],
    [1, 3, 5, 6],
    [6, 2, 4, 4, 5],
    [9, 5, 3, 5, 5, 7],
    [7, 4, 6, 4, 7, 6,8]
]

def find_max_gold (mount):
    calculate_floor = mount[0]
    for i in range(len(mount) - 1):
        floor_one = calculate_floor
        floor_two = mount[i+1]
        calculate_floor = fill_floor(floor_one,floor_two)
    return max(calculate_floor)

def fill_floor(floor_one, floor_two):
    result = []
    for i in range(len(floor_two)):
        result.append(0)
    for i in range(len(floor_one)):
        if result[i] < floor_one[i] + floor_two[i]:
            result[i] = floor_one[i] + floor_two[i]
        result [i+1] = floor_one[i] + floor_two[i+1]
    return result

max_gold = find_max_gold(mount)
print("Max gold = ",max_gold)        