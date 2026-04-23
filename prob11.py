# Take a string and print each character one by one using loop

n = input("Enter the String: ") #accepted the string from the User

# print(n)

for i in range(0,len(n)): #use length of the string i.e len(n) to get the exact length of the string 
    #range(0,len(n)) => start from the zero to the last character of the string n
    print(n[i]) #gives each character
    #print the value of n[i] i.e the character at i index