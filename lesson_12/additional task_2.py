def load_str_from_file(file_name):
    user_file = open(file_name,"r")
    result = user_file.read()
    user_file.close()
    return result

def intersection_of_text(text_1, text_2):
    set_1 = set(text_1.split(" "))
    set_2 = set(text_2.split(" "))
    result_set = set_1.intersection(set_2)
    return result_set

def save_set_to_file(file_name, result):
    user_file = open(file_name,"w")
    for element in result:
        user_file.write(element+"\n")
    user_file.close()

file_1 = "additional task_2_a_file.txt"
file_2 = "additional task_2_b_file.txt"

text_1 = load_str_from_file(file_1)
text_2 = load_str_from_file(file_2)

result = intersection_of_text(text_1, text_2)

save_set_to_file("result.txt",result)
