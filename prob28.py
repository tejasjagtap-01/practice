# Q4. Create a program that prints the multiplication table of a given number.

s = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{s} X {i} = {s*i}")

