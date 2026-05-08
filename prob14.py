# Count length of string (without using len())

# 👉 Use loop

n = input("Enter the string: ")

count = 0 

for ch in n:
    count += 1

print(f"Length of String: {count}")


s = input("Enter the string: ")

count = 0


# for i in range(0, 1000):   # assume max length
#     if i < len(s):         # using len just for safety here
#         count += 1

# print(count)