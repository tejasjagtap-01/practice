#  Create a calculator app using if-else

print("Welcome to the Calculator")

num1 = int(input("Enter the Number 1 : "))
num2 = int(input("Enter the Number 2 : "))


print("The Selction: ")
print("1. Addittion ")
print("2. Subtraction ")
print("3. Multiplication")
print("4. Divide")

choice = int(input("Enter the Choice (1,2,3,4).strip()"))

if choice == 1:
    result = num1 + num2
    print(f"The sum of {num1} number  with number {num2} is {result} ")
elif choice == 2:
    result = num1- num2
    print(f"The sutraction of {num1} number  with number {num2} is {result} ")
elif choice == 3:
    result = num1 * num2
    print(f"The multiplication of {num1} number  with number {num2} is {result} ") 
elif choice == 4:
    result = num1 / num2
    print(f"The ation of {num1} number  with number {num2} is {result} ") 
else:
    print("Invalid Choice")