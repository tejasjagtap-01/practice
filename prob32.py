#  Create a program to count the number of vowels in a string

s = input("Enter the String: ")

vowel = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowel += 1
print("The Total Count",vowel)