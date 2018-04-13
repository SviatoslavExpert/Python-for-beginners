def load_str_from_file(file_name):
    user_file = open(file_name, "r")
    result = user_file.read()
    user_file.close()
    return result

def count_letter(text, letter):
    count = 0
    for element in text:
        if element == letter:
            count = count + 1
    return count

file_name = "task_2_file.txt"

text = load_str_from_file(file_name)

count = count_letter(text, "A")

print("A = ", count)
    
