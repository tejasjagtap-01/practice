# Count digits, alphabets, and special characters

s = input("Enter the String: ")

alpha = 0
dig = 0
sp = 0
for ch in s:
    if ch.isalpha():
        alpha += 1 

    elif ch.isdigit():
        dig += 1

    else:
    sp += 1


print(f"The Alphabet count is : {alpha}")
print(f"The Digit count is : {dig}")
print(f"The Special Character count is : {sp}")