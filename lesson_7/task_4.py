import math
for i in range(10):
    result = "{:.{number}f}".format(math.pi,number =(2+i))
    print(result)