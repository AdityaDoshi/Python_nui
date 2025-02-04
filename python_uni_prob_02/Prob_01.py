def largest_smallest(a, b):
    if a>b:
       print("largest:",a)
       print("smallest:",b)
    else:
        print("largest:",b)
        print("smallest:",a)

a = int(input("Enter a number"))
b = int(input("Enter another number"))

largest_smallest(a, b)

