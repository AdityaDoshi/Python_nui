import math
def position_point(x1, x2, y1, y2, r):
    dist= math.sqrt((x2-x1)**(2)+(y2-y1)**(2))
    if dist<r:
        print("The point is inside the circle")
    elif dist>r:
        print("The point is outside the circle")
    else:
        print("The point is on the circle")


x1 = 0
y1 = 0
r = 10
x2 = int(input("Enter the x coordinate of the point"))
y2 = int(input("Enter the y coordinate of the point"))
position_point(x1, x2, y1, y2, r)