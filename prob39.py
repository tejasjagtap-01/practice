#  Write a Python script to reverse a given string

s = input("Enter the Character: ")

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("It is not Valid Palindrome")
        break
    else:
        print("It is Valid Palindrome")
        break
    