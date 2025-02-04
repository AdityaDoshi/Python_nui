def remove_substring(str1, str2):
    return str1.replace(str2, '')

str1 = "abcdef"
str2 = "cd"
str3 = remove_substring(str1, str2)

print("Final String:", str3) 
