name = input("Input name: ")
is_name = True
if name[0].islower() or name[0].isdigit():
    is_name = False
for letter in name[1:]:
    if letter.isupper() or letter.isdigit():
        is_name = False
print(name, "it is a name -> ", is_name)