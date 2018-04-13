number_one = int(input("Input number one: "))
number_two = int(input("Input number two: "))
number_three = int(input("Input number three: "))
number_four = int(input("Input number four: "))
max_number = number_one
if number_two > max_number:
    max_number = number_two
if number_three > max_number:
    max_number = number_three
if number_four > max_number:
    max_number = number_four
print("Max = ",max_number)

