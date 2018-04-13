money_text = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety"
}

my_money = input("How much money do you have? ")
money_part = []
money = my_money.split(",")
part = 1000000
dollars = int(money[0])
result = ""
while part > 0:
    money_part.append(dollars // part)
    dollars = dollars % part
    part = part // 1000

for i in range(len(money_part)):
    temp_part = money_part[i]
    if temp_part == 0:
        continue
    hundred = temp_part // 100
    if hundred > 0:
        result += money_text.get(hundred)+" huntred"
    decimal = temp_part % 100
    if decimal <= 20 and decimal > 0:
        result +=" " + money_text.get(decimal)
    else:
        dec = decimal // 10
        result += " " + money_text.get(10 * dec)
        one = decimal % 10
        if one > 0:
            result += " " + money_text.get(one)
    if i == 0:
        result += " million "
    if i == 1:
        result += " thousand "

if len(result) > 1:
    result += " dollars"
if len(money) > 1:
    cent = money[1]
    if len(cent) == 1:
        cent = int (cent) * 10
    else:
        cent = int(cent)
    if cent <= 20 and cent > 0:
        result +=" " + money_text.get(cent)
    else:
        dec = cent // 10
        result += " " + money_text.get(10 * dec)
        one = cent % 10
        if one > 0:
            result += " " + money_text.get(one)
    if cent > 0:
        result += " cent"

print(result)
