# Check if a given year is a leap year or not

n = int(input("Enter the Year: "))

if (n % 4 == 0 or n % 400 == 0 or n % 100 != 0):
    print("The Year is Leap Year! ")
else:
    print("The Year is not Leap Year! ")
