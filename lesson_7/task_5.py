text = input("Input text: ")
words = list(text.split(" "))
long_word = words[0]
for word in words:
    if len(word) > len(long_word):
        long_word = word
print("Longest word is: ",long_word)