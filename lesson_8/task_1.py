day_of_the_week = {
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
}

day_number = int(input(" Input day number:  "))

print(day_number, " -> ", day_of_the_week.get(day_number))
