text = input("Input words: ")
word = "error"
for i in range(1, len(text)//2 + 1):
    if len(text)%i != 0:
        continue
    num = len(text)//i
    temp_word = text[:i]
    if (temp_word*num) == text:
        word = temp_word
        break
print("Vovochka write -> ", word)
