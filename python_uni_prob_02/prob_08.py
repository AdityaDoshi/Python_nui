def valid_triangle(a, b, c):
    if a+b+c==180:
        print("Valid triangle")
    else:
        print("Not a valid triangle")

a = int(input("Enter a length of a triangle"))
b = int(input("Enter a length of a triangle"))
c = int(input("Enter a length of a triangle"))

valid_triangle(a, b, c)