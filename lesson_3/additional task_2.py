x = float(input("Input x coordinate: "))
y = float(input("Input y coordinate: "))

a_x = 0
a_y = 0
b_x = 4
b_y = 4
c_x = 6
c_y = 1

mult_a = (a_x - b_x) * (a_y - y) - (a_y - b_y) * (a_x - x)
mult_b = (b_x - c_x) * (b_y - y) - (b_y - c_y) * (b_x - x)
mult_c = (c_x - a_x) * (c_y - y) - (c_y - a_y) * (c_x - x)

if (mult_a <= 0 and mult_b <= 0 and mult_c <= 0) or  (mult_a >= 0 and mult_b >= 0 and mult_c >= 0):
     print("Point (x = ", x ,",  y = ", y ,") ", " in the triangle")
else:
     print("Point (x = ", x ,",  y = ", y ,") ", " outside the  triangle")
