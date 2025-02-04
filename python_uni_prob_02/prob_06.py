def digits(num):
    number_digit = len(str(num))
    return number_digit
num = int(input("Enter a number"))
dig = digits(num)
print("The digit of the given number is:", dig)