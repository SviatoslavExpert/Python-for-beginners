def get_age_description(age):
    if 0 < age < 10:
        return "детский возраст"
    elif 10 <= age < 25:
        return "юный возраст"
    elif 25 <= age < 44:
        return "молодой возраст"
    elif 44 <= age < 60:
        return "средний возраст"
    elif 60 <= age < 75:
        return "пожилой возраст"
    elif 75 <= age < 90:
        return "старческий возраст"
    elif 90 <= age:
        return "возраст долгожителя"
    else:
        return "Неизвестный возраст"

name = input("Input your name:  ")
age = int(input("Input your age:  "))
print(name," у вас ", get_age_description(age))