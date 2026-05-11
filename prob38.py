#  Create a number guessing game. 
import random

secret_no = random.randint(1,10)
attempt = 0

while True:
    try:
        s = int(input("Enter the number: "))
        attempt += 1
        
        if secret_no == s:
            print("The Guess is right")
            break
        elif secret_no != s:
            print("It's worng guess")
    except ValueError:
        prinit(f"Please enter the Right Choice")