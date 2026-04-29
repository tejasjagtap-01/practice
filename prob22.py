# Replace vowels with *
#assisted by ChatGpt


s = input("Enter the String: ") #accept user input 

result = "" #stores the the empty string to string to store result

for ch in s: #loop through each character of the string
    if ch in "aeiouAEIOU": #check for vowels
        result += "*" #replace vowel with *
    else:
        result += ch #keep character as it is

print(result) #print final modified output