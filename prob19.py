# Count frequency of characters

s = input("Enter the string: ")

freq = {} # it creates dictionary to store 
#() creates a tuple, not a dictionary → tuple is immutable

for ch in s:
    #character already exists → increase count
    if ch in freq:
        freq[ch] += 1
    #character comes first time → set count = 1
    else:
        freq[ch] = 1
    
#key means each character stored in dictionary
for key in freq: 
    print(key, ":", freq[key])