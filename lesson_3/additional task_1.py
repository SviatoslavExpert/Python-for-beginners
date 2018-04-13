x = float(input("Input x coordinate: "))
y = float(input("Input y coordinate: "))
r = 4
if x**2 + y**2 <= r**2:
    print("Point (x = ", x ,",  y = ", y ,") ", " in the circle")
else:
    print("Point (x = ", x ,",  y = ", y ,") ", " outside the circle")
