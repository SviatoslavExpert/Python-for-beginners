def save_list_to_file(file_name, user_list):
    file_save = open(file_name,"w")
    file_save.write("[")
    for element in user_list:
        file_save.write(str(element)+" ")
    file_save.write("]")
    file_save.close()
    return

file_name = "task_1_file.txt"
user_list = [7, 5, 11, 23, -2]

save_list_to_file(file_name,user_list)
