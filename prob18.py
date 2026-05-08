# Check Palindrome

x = input("Enter the string: ")

rev = "" #Initializes an empty string 

for ch in x:
    rev = ch + rev #add each character to the front
    #store the reverse of X in rev 

if x == rev:
    print("Palindrome")
else:
    print("Not Palindrome")