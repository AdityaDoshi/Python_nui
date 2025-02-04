x1 = int(input("Enter x co-ordinate of first point "))
y1 = int(input("Enter y co-ordinate of first point "))
x2 = int(input("Enter x co-ordinate of second point "))
y2 = int(input("Enter y co-ordinate of second point "))
x3 = int(input("Enter x co-ordinate of third point "))
y3 = int(input("Enter y co-ordinate of third point "))
if ((y2-y1)/(x2-x1))==((y3-y2)/(x3-x2)):
    print("All the points lie on the same line")
else:
    print("all the points don't lie on the same line")