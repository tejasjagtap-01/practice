# Find largest and smallest character (ASCII based)

s = input("Enter the String: ")

lower = s[0]
highest = s[0]

for ch in s:
    if ch > highest:
        highest = ch 

    if ch < lower:
        lower = ch 
    
print(f"The Largest number is {highest}")
print(f"The Largest number is {lower}")