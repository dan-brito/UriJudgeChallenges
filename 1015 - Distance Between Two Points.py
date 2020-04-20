from math import sqrt

point1 = input().split(" ")
x1, y1 = point1
point2 = input().split(" ")
x2, y2 = point2

# distance = abs((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1) ** 2))
distance = (float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2
distance_square = sqrt(distance)


print('%0.4f' % distance_square)



