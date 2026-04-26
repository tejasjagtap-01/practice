# Count consonants

str = input("Enter the string: ")

count = 0

for ch in str:
    if ch in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        count +=1

print(count)