def concat(int_number, float_number, text):
    return text + str(int_number + float_number)

text = concat(3, 3.5, "Hello world ")

print(text)