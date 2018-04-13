def input_text():
    result = ""
    print("Input text line. Type exit to end input text:")
    while True:
        text = input()
        if text == "exit":
            break
        result += text + "\n"
    return result

def save_str_to_file(text, file_name):
    user_file = open(file_name,"w")
    user_file.write(text)
    user_file.close()


file_name = "task_3_file.txt"

text = input_text()
save_str_to_file(text,file_name)
