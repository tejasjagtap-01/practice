# Write a program to find the GCD of two numbers.

def gcd(a, b):
    while b != 0:
        a,b = b, a%b
    return a

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))


result = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {result}")