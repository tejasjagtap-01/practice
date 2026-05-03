# Q5. Write a program to find the largest of three numbers. 

s1 = int(input("Enter the number1 : "))
s2 = int(input("Enter the number2 : "))
s3 = int(input("Enter the number3 : "))

if(s1 == s2 == s3):
    print(f"The number1 {s1} , Number2 {s2} and Number{s3} are equal!")
elif(s1 >= s2 and s1 >= s3):
    print(f"The Number 1 {s1} is greater than {s2} and {s3}")
elif(s2 >= s1 and s2 >= s3):
    print(f"The Number 2 {s2} is greater than {s1} and {s3}")
else:
    print(f"The Number 3 {s3} is greater than {s1} and {s2 }")