# Remove spaces from string

s = input("Enter the string: ")

result = ""

for ch in s: # Loop runs character by character
    if ch != " ": #If it is a space → ignore it
        result += ch

print(result)