def largest_smallest(a, b, c):
    largest = max(a, b, c)
    smallest = min(a, b, c)
    return largest, smallest
    

a = int(input("Enter a number"))
b = int(input("Enter another number"))
c = int(input("Enter another number"))
largest, smallest = largest_smallest(a, b, c)
print("Largest=",largest)
print("smallest=",smallest)

largest_smallest(a, b, c)