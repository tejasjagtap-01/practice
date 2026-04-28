# Remove spaces from string

s = input("Enter the string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)