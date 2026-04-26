# Count consonants

s = input("Enter the string: ")

count = 0

for ch in s:
    if ch in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        count +=1

print(count)