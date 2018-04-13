def load_str_from_file(file_name):
    user_file = open(file_name,"r")
    result = user_file.read()
    user_file.close()
    return result

def get_statistic(text):
    text = text.upper()
    result = {}
    for letter in text:
        if letter.isalpha():
            count = result.get(letter)
            if count is None:
                result[letter] = 1
            else:
                result[letter] = count + 1
    return result

def print_statictic (statistic):
    while statistic:
        key_list = list(statistic.keys())
        letter = key_list[0]
        count = statistic.get(letter)
        for let in statistic:
            col = statistic.get(let)
            if count < col:
                letter = let
                count = col
        print(letter," -> ",count)
        statistic.pop(letter)

file_name = "additional task_1_file.txt"

text = load_str_from_file(file_name)
statistic = get_statistic(text)
print_statictic(statistic)
    
