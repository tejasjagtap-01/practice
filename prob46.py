# Write a program to display the ASCII value of a character. 

#user input
user_input = input("Enter the Character: ")

#check if user actually typed exactly one character!
if(len(user_input)) == 1:
    ascii_value = ord(user_input) #ord() convert sigle character into numerical ascii

    print(f"The Ascii value of {user_input} is {ascii_value}")

else:
    print("Oops! Please enter actual runber")