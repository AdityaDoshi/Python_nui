def compare_string(str1, str2):
    if str2 in str1:
        print("The second string is in first string")
    else:
        print("The second string is not in first string")


str1 = input("Enter first string")       
str2 = input("Enter second string")       
compare_string(str1, str2)