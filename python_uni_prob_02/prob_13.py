def num_to_words(num):
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
             "eighteen", "nineteen"]
    if 0<=num<=19:
        return word[num]
    else:
        return "number out of range"
num=int(input("Enter a number"))
word=num_to_words(num)
print("The number is:",word)