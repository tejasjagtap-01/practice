# Count vowels in a string

a = input("Enter the string: ")

count = 0

for ch in a:
    if ch in "aeiouAEIOU":
        count += 1

print("Total length ", count)

# a = input("Enter the string: ")
# count = sum(1 for ch in a if ch in "aeiouAEIOU")
# print("Total vowels:", count)