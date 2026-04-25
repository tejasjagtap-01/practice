# Count length of string (without using len())

# 👉 Use loop

n = input("Enter the string: ")

count = 0 

for ch in n:
    count += 1

print(f"Length of String: {count}")