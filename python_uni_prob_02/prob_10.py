def area_para(l,b):
    area=l*b
    parameter=2*(l+b)
    if area>parameter:
        print("The area of the given rectangle is greater than it's parameter")
    else:
        print("The area of the given rectangle is not greater than it's parameter")
l = int(input("Enter the length of the rectangle"))
b = int(input("Enter the bredth of the rectangle"))
area_para(l,b)