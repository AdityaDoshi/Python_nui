def count_vowel(str):
    vowel = "aeiouAEIOU"
    count=0
    for char in str:
        if char in vowel:
          count+=1
    print(f"there are {count}number of vowels in the given string")


str = input("Enter a string:")
count_vowel(str)