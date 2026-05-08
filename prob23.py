# Count digits, alphabets, and special characters

s = input("Enter the String: ")

alpha = 0 #Count Alphabet
dig = 0 #Count Digit
sp = 0 #Count Special Character

for ch in s: #Loop through each character
    if ch.isalpha(): #check if character is alphabet
        alpha += 1 

    elif ch.isdigit(): #check if character is digit or not
        dig += 1

    else: #neither alphabet nor character 
        sp += 1


print(f"The Alphabet count is : {alpha}")
print(f"The Digit count is : {dig}")
print(f"The Special Character count is : {sp}")