def string_to_lower(string):
    lower_case = ''
    for char in string:
        if 'A'<= char <='Z':
            lower_case += chr(ord(char) + 32)
        else:
            lower_case += char
    return lower_case
def string_to_upper(string):
    upper_case = ''
    for char in string:
        if 'a'<= char <='z':
            upper_case += chr(ord(char) - 32)
        else:
            upper_case += char
    return upper_case
def string_to_toggle(string):
    toggle_case = ''
    for char in string:
        if 'a'<= char <='z':
            toggle_case += chr(ord(char) - 32)
        elif 'A'<= char <='Z':
            toggle_case += chr(ord(char)+32)
        else:
            toggle_case += char    
    return toggle_case

string= input("Enter your string:")
lower_case = string_to_lower(string)
upper_case = string_to_upper(string)
toggle_case = string_to_toggle(string)
print(lower_case)
print(upper_case)
print(toggle_case)