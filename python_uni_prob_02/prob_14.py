def marks_assignment(math, sci, comp):
    total=math+sci+comp
    avg=total/3
    if math < 39 or sci < 39 or comp < 39:
        print("Fail")
    else:
        print("Pass")
    if 80<=math<=100:
        print("The grade in math is: O")
    elif 70<=math<=79:
        print("The grade in math is: A+")
    elif 60<=math<=69:
        print("The grade in math is: A")
    elif 55<=math<=59:
        print("The grade in math is: B+")
    elif 50<=math<=54:
        print("The grade in math is: B")
    elif 45<=math<=49:
        print("The grade in math is:C")
    elif 40<=math<=44:
        print("The grade in math is: P")
    else:
        print("The grade in math is: f")
    if 80<=sci<=100:
        print("The grade in sci is: O")
    elif 70<=sci<=79:
        print("The grade in sci is: A+")
    elif 60<=sci<=69:
        print("The grade in sci is: A")
    elif 55<=sci<=59:
        print("The grade in sci is: B+")
    elif 50<=sci<=54:
        print("The grade in sci is: B")
    elif 45<=sci<=49:
        print("The grade in sci is:C")
    elif 40<=sci<=44:
        print("The grade in sci is: P")
    else:
        print("The grade in sci is: f")
    if 80<=comp<=100:
        print("The grade in comp is: O")
    elif 70<=comp<=79:
        print("The grade in comp is: A+")
    elif 60<=comp<=69:
        print("The grade in comp is: A")
    elif 55<=comp<=59:
        print("The grade in comp is: B+")
    elif 50<=comp<=54:
        print("The grade in comp is: B")
    elif 45<=comp<=49:
        print("The grade in comp is:C")
    elif 40<=comp<=44:
        print("The grade in comp is: P")
    else:
        print("The grade in comp is: f")
math=int(input("Enter the marks of maths:"))
sci=int(input("Enter the marks of sci:"))
comp=int(input("Enter the marks of comp:"))
marks_assignment(math, sci, comp)