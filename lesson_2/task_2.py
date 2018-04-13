import math
side_a = 0.3
side_b = 0.4
side_c = 0.5
half_perimetr = (side_a + side_b + side_c)/2
area = math.sqrt(half_perimetr *(half_perimetr -side_a)*(half_perimetr -side_b)*(half_perimetr -side_c))
print("Area = ",area)

