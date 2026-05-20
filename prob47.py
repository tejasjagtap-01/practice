# Convert a decimal number to binary using loops.

def decimal_to_binary(decimal_num):
    #handle the base case where the number is 0
    if decimal_num == 0:
        return "0"
    
    binary_string = ""

    #Loop until divide the number down to 0
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_string += str(remainder) #collect the remainder
        decimal_num = decimal_num // 2 #Integer division to update number

    #Reverse the string because the remainder were found in reverse order
    return binary_string[::-1]

#For user Input
user_number = int(input("Enter a decimal number: "))

#pass the user number to function and save the result
result = decimal_to_binary(user_number)

#print the final result
print(f"The binary representation is: {result}")