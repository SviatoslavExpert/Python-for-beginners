text = input("Input text:  ")
statistic = {}
for letter in text:
    if letter.isalpha():
        count = statistic.get(letter)
        if count is None:
            statistic[letter] = 1
        else:
            statistic[letter] = count + 1
print(statistic)
