# Check Palindrome

x = input("Enter the string: ")

rev = ""

for ch in x:
    rev = ch + rev

if x == rev:
    print("Palindrome")
else:
    print("Not Palindrome")