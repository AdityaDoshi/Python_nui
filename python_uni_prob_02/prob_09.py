def absolute_value(a):
    if a<0:
        a=-a
        print("Absolute value of the given number is:", a)
    else:
        print("Absolute value of the given number is:", a)

a = int(input("Enter a value"))
absolute_value(a)