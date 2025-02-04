def leap_year(a):
    if a%4==0:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
a=int(input("Enter a year"))
leap_year(a)