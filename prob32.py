#  Create a program to count the number of vowels in a string

s = input("Enter the String: ")  # Take input string from user

vowel = 0 # Variable to store count of vowels

# Loop through each character in the string
for ch in s:
    if ch in "aeiouAEIOU":  # Check if character is a vowel (both lowercase and uppercase)
        vowel += 1 # Increase vowel count by 1
        
print("The Total Count",vowel)