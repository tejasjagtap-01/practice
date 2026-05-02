# Q1. Write a Python program to swap two variables.

s = int(input("Enter the number 1: "))

t = int(input("Enter the number 2: "))

temp = s
s = t 
t = temp

print(f"The number1 is {s} and number2 is {t}")