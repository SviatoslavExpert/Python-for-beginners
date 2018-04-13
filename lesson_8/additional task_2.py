rome_number = {
 "I":1,
 "V":5,
 "X":10,
 "L":50,
 "C":100   
}
number = input("Input rome number:  ")
result_number = [0]
for num in number:
    temp_number = rome_number.get(num)
    if temp_number > result_number[len(result_number)-1]:
        result_number[len(result_number)-1] = temp_number - result_number[len(result_number)-1]
    else:
        result_number.append(temp_number)

dec_number = sum(result_number)
print(number, " -> ", dec_number)
