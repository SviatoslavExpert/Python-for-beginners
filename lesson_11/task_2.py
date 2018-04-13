def draw_triangle(heigth,symbol = "#"):
    for i in range(heigth):
        print(symbol*(i + 1))

draw_triangle(4)

draw_triangle(5,"*")