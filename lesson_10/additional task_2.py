def is_pal(number):
    text_number = str(number)
    if text_number == text_number[::-1]:
        return True
    else:
        return False

first_number = 100
second_number = 100
max_pal = first_number * second_number

for i in range(999,100,-1):
    for j in range(i,100,-1):
        if i * j > max_pal and is_pal(i*j):
            max_pal = i * j
            first_number = i
            second_number = j

print(max_pal," = ",first_number," x ",second_number)