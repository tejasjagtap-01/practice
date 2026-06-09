#Palindrome Question

s = input("Enter the String: ")

left = 0
right = len(s)-1
is_Palindrome = True

while left < right:
    if s[left] != s[right]:
        is_Palindrome = False
        break
    left += 1
    right -= 1
        
if is_Palindrome:    
    print("It is Palindrome")
else:
    print("It is not Palindrome")