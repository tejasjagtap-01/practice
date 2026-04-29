# First non-repeating character
#assisted by ChatGpt

s = input("Enter the String: ") #accepts the user values

freq = {} #create empty dictionary to store frequency 

#counts frequency of each character
for ch in s: #loop through each character in string
    if ch in freq: #if character already existed in dictionary 
        freq[ch] += 1 #increase its count
    else:
        freq[ch] = 1 #if first step set count = 1

#find first non repeating characters
for ch in s: #loop again in original order
    if freq[ch] == 1: #check if frequency is 1
        print("First non-repeating: ",ch) 
        break # Stop after finding the first one 