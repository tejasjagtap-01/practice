#  Write a program to calculate the factorial of a number using a loop. 

# a = int(input("Enter the input: "))

# fact = 0

# if a < 0:
#     print("The factorial of negatice number is not exist")
# else:
#     i = 1
#     while i <= a:
#         fact *= i
#         i =+ 1
#         print(f"The factorial of number {a} is {fact}")

# Python program to find factorial using while loop

# # Take input from user
# num = int(input("Enter a non-negative integer: "))

# # Initialize result
# factorial = 1

# # Check for negative numbers
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# else:
#     i = 1
#     while i <= num:
#         factorial *= i
#         i += 1
#         print(f"The factorial of {num} is {factorial}")

a = int(input("Enter the input: "))

fact = 1  # Changed from 0 to 1

if a < 0:
    print("The factorial of a negative number does not exist.")
elif a == 0:
    print("The factorial of 0 is 1")
else:
    i = 1
    while i <= a:
        fact *= i
        i += 1  # Changed from =+ to +=
    
    # Moved the print outside the loop to only show the final result
    print(f"The factorial of number {a} is {fact}")