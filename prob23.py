# Count digits, alphabets, and special characters

s = input("Enter the String: ")

alpha = ""
dig = ""
sp = ""

for ch in s:
    if ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alpha =+ alpha
    if ch in '0987654321':
        dig =+ dig
    if ch in '!@#$%^&*':
        sp =+ sp

print(f"The Alphabet count is : {alpha}")
print(f"The Digit count is : {dig}")
print(f"The Special Character count is : {sp}")