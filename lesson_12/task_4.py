def load_str_from_file(file_name):
    user_file = open(file_name, "r")
    result = user_file.read()
    user_file.close()
    return result

def split_text (text):
    result = text.split(" ")
    return result

def get_longest_word (words_list):
    result = words_list[0]
    for word in words_list:
        if len(word) > len(result):
            result = word
    return result


file_name = "task_4_file.txt"

text = load_str_from_file(file_name)
words_list = split_text(text)
word = get_longest_word(words_list)
print(word)    
